"""
CURRENT THINKING

The environemnt is dependent on the state space.
then the state space should be injected into the environment.
"""

from State import State

from typing import Type
from Action import Action

class StateSpace(dict[int, State]):
    """Environmnet State Space dependency."""

    def __init__(self,
                 number_of_states: int,
                 terminal_states_rewards: dict[int, int],
                 state_class: Type[State] = State
                ) -> None:
        for state in range(number_of_states):
            self[state] = state_class()

        # Terminal states & their rewards.
        # TODO StateSpaceService.
        self.set_terminal_states_rewards(terminal_states_rewards)
        
        # TODO StateSpaceService.
        self.set_actions()

    def __getattr__(self, key: int):
        if key in self:
            return self[key]
        else:
            raise AttributeError(f"'StateSpace' object has not attribute '{key}'")
 
    # TODO StateSpaceService.
    def set_terminal_states_rewards(self, terminal_state_rewards: dict[int, int]) -> None:
        """Set the rewards & terminal properties for the terminal States."""
        
        for state in terminal_state_rewards:
            self[state].reward = terminal_state_rewards[state]
            self[state].is_terminal = True

    # TODO StateSpaceService.
    def set_actions(self) -> None:
        """Set the possible actions for each State in the State Space."""
        
        for state in self:
            # Check if State is terminal. (Terminal States will have no actions).
            if not self[state].is_terminal:
                
                # Check if the State can move right.
                if state < len(self) - 1:
                    self[state].actions.append(Action.right)
                
                # Check if the State can move left.
                if state > 0:
                    self[state].actions.append(Action.left)
