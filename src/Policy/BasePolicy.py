"""
Base Policy type for a reinforcement learning agent.

Policy type is a mapping from a State Index to the State's
Action Probability Distribution.
A State's Action Probability Distribution is a mapping of available Actions to 
their probability of being taken by the Policy.
"""

from abc import ABC, abstractmethod
from typing import Dict

from src.ActionProbabilityDistribution import ActionProbabilityDistribution
from src.StateIndex import StateIndex # type: ignore
from src.Action import Action


class BasePolicy[StateIndex, A: Action](ABC, Dict[StateIndex, ActionProbabilityDistribution[A]]):
    @abstractmethod
    def choose_action(self, state: StateIndex) -> A:
        """
        Policy selects an action for the given State according to the State's
        Action Probability Distribution & the goal of the Policy.
        """
 
        pass

    @abstractmethod
    def get_action_probability_distribution(self, state: StateIndex) -> ActionProbabilityDistribution[A]:
        """Return the Action Probability Distribution for the given state."""
        
        return ActionProbabilityDistribution(self[state])
    
    def set_new_state_policy(self,
                             state: StateIndex,
                             new_action: A
                            ) -> None:
        """Set a new Policy for given State."""
        
        state_action_probability_distribution: ActionProbabilityDistribution[A] = self.get_action_probability_distribution(state)
        
        for action in state_action_probability_distribution:
            if action == new_action:
                self[state][action] = 1
            else:
                self[state][action] = 0
