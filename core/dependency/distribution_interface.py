from abc import ABC, abstractmethod
from typing import Dict

class DistributionInterface[K, V](ABC, Dict[K, V]):
    """Distribution Abstract Base Class for standardising distributions 
    throughout reinforcement learning problems.
    
    Used by:
        ProbabilityDistribution to set probabilities of a State occuring.
        # TODO Below not true yet.
        # StateActions to set the distribution of Actions available to a State 
        # to the probability distribution of next States that could occur, 
        # define in StateProbabilityDistribution.
    """

    @abstractmethod
    def __init__(
        self,
        distribution: Dict[K, V]
    ) -> None:
        super().__init__(distribution)

    @abstractmethod
    def set_distribution(
        self,
        distribution: Dict[K, V]
    ) -> None:
        pass

    @abstractmethod
    def set_distribution_for_key(
        self,
        key: K,
        distribution: V
    ) -> None:
        pass

    @abstractmethod
    def get_distribution(
        self
    ) -> Dict[K, V]:
        pass

    @abstractmethod
    def get_distribution_of_key(
        self,
        key: K
    ) -> V:
        pass
