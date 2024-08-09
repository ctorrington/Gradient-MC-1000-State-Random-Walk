"""Grid World Environment."""

# from typing import Dict

from core.environment.environment import Environment
from core.dependency.state_actions import StateActions
from core.dependency.state_probability_distribution import StateProbabilityDistribution
from log.ilogger import ILogger

from solutions.grid_world.state_space import GridWorldStateSpace
from solutions.grid_world.action import GridWorldAction
from solutions.grid_world.state_index import GridWorldStateIndex


# Grid World State Space representation.

# 00 01 02 03
# 04 05 06 07
# 08 09 10 11
# 12 13 14 15

class GridWorldEnvironment(Environment[GridWorldStateIndex, GridWorldAction]):
    def __init__(
        self,
        state_space: GridWorldStateSpace,
        logger: ILogger
    ) -> None:
        
        super().__init__(
            state_space=state_space
        )
        
        # TODO fix these overriding errors.
        # self.state_space: GridWorldStateSpace = state_space
        self.initialize_environment()
        
    def initialize_environment(self) -> None:
        # TODO Doc string.
        
        for state in self.state_space:

            state_actions: StateActions[GridWorldStateIndex, GridWorldAction] = self.determine_state_actions(state)
            self[state] = state_actions
            
    def determine_state_actions(
        self, 
        state: GridWorldStateIndex
    ) -> StateActions[GridWorldStateIndex, GridWorldAction]:
        """Determine the Actions available for each State."""
        
        # TODO Figure out defaultdict for this.
        state_actions: StateActions[GridWorldStateIndex, GridWorldAction] = {}
        
        for action in self.state_space[state].actions:
            
            possible_next_states_distribution: Dict[GridWorldStateIndex, float] = self.determine_next_state_probability_distribution(state, action)
            state_actions[action] = possible_next_states_distribution
            # TODO understand why update method returns KeyErorr.
            # state_actions[action].update(possible_next_states_distribution)
            
        return state_actions
    
    # def set_actions_for_state_index(
    #     self,
    #     state_index: GridWorldStateIndex,
    #     action: 
    # )
    
    # def set_state_action_probability_distribution(
    #     self,
    #     state_index: GridWorldStateIndex
    # ) -> StateProbabilityDistribution[GridWorldStateIndex]:
    #     """_summary_

    #     Args:
    #         state_index (GridWorldStateIndex): _description_

    #     Returns:
    #         StateProbabilityDistribution: _description_
    #     """
        
        # for (state_index, state) in self.state_space.items():
            
        #     for action in state.actions:
                
                
        
        # pass
            
    def determine_next_state_probability_distribution(
        self,
        state: GridWorldStateIndex,
        action: GridWorldAction
    ) -> StateProbabilityDistribution[GridWorldStateIndex]:
        """
        Return a mapping of the possible next States & their probability of
        occuring.
        
        In this Grid World, Actions are deterministic.
        Up will only go up (if possible).
        
        If an Action would take the Agent off the State Space, then the next 
        state is the State the Agent is currently in. This happens with 
        probability 1.
        """
        
        # TODO error checking State is correct type for Grid World problem.
        # TODO service class.
        row, column = state
        # TODO defaultdict.
        possible_next_states: StateProbabilityDistribution[GridWorldStateIndex] = {}
        
        match action:
            case GridWorldAction.UP:
                if row > 0:
                    possible_next_states[row - 1, column] = 1.0
                else:
                    possible_next_states[row, column] = 1.0
                    
            case GridWorldAction.DOWN:
                if row < self.state_space.number_of_rows - 1:
                    possible_next_states[row + 1, column] = 1.0
                else:
                    possible_next_states[row, column] = 1.0
                
            case GridWorldAction.LEFT:
                if column > 0:
                    possible_next_states[row, column - 1] = 1.0
                else:
                    possible_next_states[row, column] = 1.0
                
            case GridWorldAction.RIGHT:
                if column < self.state_space.number_of_columns - 1:
                    possible_next_states[row, column + 1] = 1.0
                else:
                    possible_next_states[row, column] = 1.0
                    
        return possible_next_states
