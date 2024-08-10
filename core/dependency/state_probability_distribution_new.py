from typing import Dict
from core.dependency.state_index import StateIndex

from core.dependency.distribution_interface import DistributionInterface

class StateProbabilityDistribution[SI: StateIndex](DistributionInterface[SI, float]):
    """Probability that a State is achieved following an Action within the 
    Environment.

    State Probability Distribution is a probability distribution of 
    successfully achieving a State following an Action from a State within the 
    Environment.
    """

    def __init__(
        self,
        distribution: Dict[SI, float]
    ):
        super().__init__(
            distribution=distribution
        )

    def set_distribution(
        self,
        distribution: Dict[SI, float]
    ) -> None:
        if not distribution:
            raise ValueError(f"Empty probability distribution provided for {self.__class__.__name__}.")
        
        self.clear()
        self.update(distribution.copy())

    def set_distribution_for_key(
        self,
        key: SI,
        distribution: float
    ) -> None:
        """Set the probability that a State occurs.

        This probability value is for a State occuring following an Action 
        from another State within the Environment.

        Args:
            key (StateIndex): State Index for the State occurring.
            distribution (float): Probability that a State occurs.
        """
        if not key in self.keys():
            raise KeyError(f"State Index {key} not within {self.__class__.__name__}.")

        self[key] = distribution

    def get_distribution(
        self
    ) -> Dict[SI, float]:
        return self

    def get_distribution_of_key(
        self,
        key: SI
    ) -> float:
        if not key in self.keys():
            raise KeyError(f"State Index {key} not within {self.__class__.__name__}.")

        return self[key]