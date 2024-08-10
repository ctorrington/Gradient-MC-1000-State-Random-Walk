from core.dependency.distribution_interface import DistributionInterface
from core.dependency.state_probability_distribution import StateProbabilityDistribution
from core.dependency.state_index import StateIndex
from core.dependency.action import Action

class StateActions[SI: StateIndex, A: Action](DistributionInterface[A, StateProbabilityDistribution[SI]]):
    """Mapping of an Action to it's State Probability Distribution. Actions can 
    result in multiple States. StateActions connects an Action within a State 
    to its StateProbabilityDistribution - the probability of next States 
    occuring.
    
    State Actions are used by an Environment to connect an Action taken in a 
    State to a distribution of possible next States.
    """
