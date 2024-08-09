from abc import ABC, abstractmethod
from typing import Dict

class ProbabilityDistributionInterface[T](ABC, Dict[T, float]):
    """Abstract Base Class for probability distributions.
    """
    
    @abstractmethod
    def __init__(
        self,
        probability_distribution: Dict[T, float]
    ) -> None:
        pass

    @abstractmethod
    def set_probability_for_key(
        self,
        key: T,
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
        key: T
    ) -> float:
        pass

    @abstractmethod
    def get_probability_distribution(
        self
    ) -> Dict[T, float]:
        pass
