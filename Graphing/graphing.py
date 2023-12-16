"""
Graphing class for UmbrellaRL package.

Currently supported graph dimensions:
    - 2D

"""

import matplotlib.pyplot as plt
from typing import List

from src.StateIndex import StateIndex
from src.Action import Action
from src.Agent.Agent import Agent
from src.StateSpace import StateSpace

class Graphing[A: Action]():
    """Graphing class for UmbrellaRL package."""
    
   # TODO overarching method that prints some dashboard with lots of lots.
    
    def __init__(self,
                 agent: Agent[StateIndex, A]
                ) -> None:
        
        # Dependencies.
        self.agent = agent
        
    def plot_state_value_function(self):
        """Plot the State Value Function of the State Space."""
        
        state_space: StateSpace[StateIndex, A] = self.agent.environment.get_state_space()
        
        z_axis_data: List[float] = self.get_z_axis_data(state_space)
        
        fig, ax = plt.subplots()
        
        ax.imshow(z_axis_data)
        
        plt.show()

    def deterine_graph_dimensionality(self,
                                      key: StateIndex
                                     ) -> int:
        """Return the dimension required to plot the graph."""
        
        if isinstance(key, tuple):
            
            return len(key)
        
        else:
            
            raise ValueError("Unsupported StateIndex type.")
