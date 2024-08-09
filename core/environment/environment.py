"""
Environment type for a reinforcement learning problem.

Environment type is a mapping from a State Index to the State's possible Actions.
"""

from abc import ABC
from typing import Dict

from core.dependency.state_index import StateIndex
from core.dependency.state_space import StateSpace
from core.dependency.state_probability_distribution import StateProbabilityDistribution
from core.dependency.state_actions import StateActions
from core.dependency.action import Action

class Environment[SI: StateIndex, A: Action](ABC, Dict[SI, StateActions[SI, A]]):
    
    def __init__(
        self,
        state_space: StateSpace[SI, A]
    ) -> None:
        self.state_space: StateSpace[SI, A] = state_space

    def get_next_states(
        self,
        current_state_index: SI,
        action: A
    ) -> StateProbabilityDistribution[SI]:
        return self.get_state_actions(current_state_index) \
            .get_state_probability_distribution(action)

    def get_state_actions(
        self,
        state_index: SI
    ) -> StateActions[SI, A]:
        return StateActions(self[state_index])

    def get_state_transition_probability(
        self,
        current_state_index: SI,
        action: A,
        next_state_index: SI
    ) -> float:
        """Return the probability of successfully transitioning from one State 
        to another State after following an Action within the Environment.

        Args:
            current_state_index (SI): State Index of the current State the 
            Agent is making an Action within.
            action (A): Action being made by the Agent.
            next_state_index (SI): State Index of the next State the Agent will 
            be in after following Action.

        Returns:
            float: Percentage probability of the next State occuring.
        """
        
        return self.get_state_actions(current_state_index) \
            .get_state_probability_distribution(action) \
                .get_state_probability(next_state_index)

    def number_of_states(self) -> int:
        """Return the number of State's in the State Space."""
        return len(self)

    def get_state_space(self) -> StateSpace[SI, A]:
        """Return the State Space."""
        return self.state_space
