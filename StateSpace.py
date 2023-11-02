"""
CURRENT THINKING

The environemnt is dependent on the state space.
then the state space should be injected into the environment.
"""

from State import State

class StateSpace(dict):
    """Environmnet State Space dependency."""
    
    def __init__(self, number_of_states: int,
                 terminal_states_rewards: dict[int, int]) -> None:
        for state in range(number_of_states):
            self[state] = State()
            
        # Terminal states.
        for state in terminal_states_rewards:
            self[state].is_terminal = True
            
        # Terminal state rewards.
        self[0].reward = -1
        self[number_of_states - 1].reward = 1
        
    def __getattr__(self, key):
        if key in self:
            return self[key]
        else:
            raise AttributeError(f"'StateSpace' object has not attribute '{key}'")
 
    def __setattr__(self, key, value):
        self[key] = value
