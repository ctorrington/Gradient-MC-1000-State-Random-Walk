from core.dependency.probability_distribution_interface import ProbabilityDistributionInterface
from core.dependency.state_index import StateIndex

class StateProbabilityDistributionNew[SI: StateIndex](ProbabilityDistributionInterface[SI]):
    pass

class StateProbabilityDistribution[SI: StateIndex](ProbabilityDistributionInterface[SI]):
    """Probability that a State is achieved following an Action within the 
    Environment.

    State Probability Distribution is a probability distribution of 
    successfully achieving a State following an Action from a State within the 
    Environment.
    """
    
    # raise DeprecationWarning

    def set_probability_distribution_for_state(
        self,
        state_index: SI,
        probability: float
    ) -> None:
        """Set the probability that a State occurs.

        This probability value is for a State occuring following an Action 
        from another State within the Environment.

        Args:
            state_index (StateIndex): State Index for the State occurring.
            probability (float): Probability that a State occurs.
        """
        if not state_index in self:
            raise KeyError(f"State Index {state_index} not within {self.__class__.__name__} for Action.")

        self[state_index] = probability

    def get_state_probability(
        self,
        state_index: SI
    ) -> float:
        """Return the probability of reaching the given State."""
        return self[state_index]
