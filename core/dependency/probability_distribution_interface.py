from abc import ABC, abstractmethod
from typing import Dict

class ProbabilityDistributionInterface[T](ABC, Dict[T, float]):
    """Abstract Base Class for probability distributions.
    """

    @abstractmethod
    def set_probability_for_key(
        self,
        state_index: T,
        probability: float
    ) -> None:
        pass

    @abstractmethod
    def set_probability_distribution(
        self,
        probability_distribution: Dict[T, float]
    ) -> None:
        pass

    @abstractmethod
    def get_probability_of_key(
        self,
        state_index: T
    ) -> float:
        pass

    @abstractmethod
    def get_probability_distribution(
        self
    ) -> Dict[T, float]:
        pass
