"""RL Agent."""

from typing import List
from copy import deepcopy

from src.ActionProbabilityDistribution import ActionProbabilityDistribution
from src.StateSpace import StateSpace
from src.Environment.Environment import Environment
from src.Policy.BasePolicy import BasePolicy
from src.StateIndex import StateIndex
from src.State import State
from src.Action import Action
from src.Agent.AgentService import AgentService
from src.Agent.History import History

# TODO Need option to improve Policy without changing the current State Space. (in place)
    # Need copy of old State Value function, improve according to those values - set State Value Function to those updated values all at once (optional, include with current implementation)

class Agent[SI: StateIndex, A: Action]:
    """RL Agent."""
    
    # TODO add method for optinally tracking the history.
    
    def __init__(
        self,
        environment: Environment[SI, A],
        policy: BasePolicy[SI, A],
        ) -> None:

        self.history = History[SI, A]()

        self.theta: float = 0.01

        self.gamma: float = 0.9

        self.environment: Environment[SI, A] = environment

        self.policy: BasePolicy[SI, A] = policy

    def evaluate_policy(self) -> None:
        """
        Evaluate the policy.

        Determine the state-value function for the policy.
        """

        state_space: StateSpace[SI, A] = self.environment.get_state_space()

        while True:

            delta = 0

            for state_index in state_space:

                if state_space[state_index].is_terminal:

                    continue

                old_state_value: float = state_space[state_index].estimated_return

                updated_state_value: float = AgentService.calculate_state_value(
                    state_index,
                    state_space,
                    self.policy,
                    self.environment,
                    self.gamma
                )

                state: State[A] = state_space.get_state(state_index)

                state.estimated_return = updated_state_value

                delta = max(delta, (abs(old_state_value - updated_state_value)))

            if delta < self.theta:

                self.history.track_state_space(state_space)

                self.history.increment_history_count()

                break

    def improve_policy(self) -> None:
        """
        Improve the Policy.

        Determine optimal actions for each State in the State Space.
        """

        state_space: StateSpace[SI, A] = self.environment.get_state_space()

        while True:

            policy_stable: bool = True

            for state_index in state_space:

                # TODO create has_actions method
                if len(state_space[state_index].actions) == 0:
                    continue

                old_state_policy: ActionProbabilityDistribution[A] = deepcopy(self.policy.get_action_probability_distribution(state_index))

                new_greedy_actions: List[A] = AgentService.determine_greedy_actions(
                    state_index,
                    state_space,
                    self.environment,
                    self.gamma
                )

                self.policy.set_new_state_policy(
                    state_index,
                    new_greedy_actions
                )

                new_state_policy: ActionProbabilityDistribution[A] = self.policy.get_action_probability_distribution(state_index)

                if old_state_policy != new_state_policy:

                    policy_stable = False

            if policy_stable:

                break

            else:

                self.evaluate_policy()
