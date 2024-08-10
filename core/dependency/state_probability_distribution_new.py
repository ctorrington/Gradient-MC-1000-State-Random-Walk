from typing import Dict
from core.dependency.state_index import StateIndex

from core.dependency.distribution_interface import DistributionInterface

class StateProbabilityDistributionNew[SI: StateIndex](DistributionInterface[SI, float]):
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