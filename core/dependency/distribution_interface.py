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

    def __init__(self, distribution: Mapping[K, V]) -> None:
        self._distribution = dict(distribution)  # Store as a dict internally

    def __getitem__(self, key: K) -> V:
        return self._distribution[key]

    def __setitem__(self, key: K, value: V) -> None:
        self._distribution[key] = value

    def __delitem__(self, key: K) -> None:
        del self._distribution[key]

    def __iter__(self):
        return iter(self._distribution)

    def __len__(self) -> int:
        return len(self._distribution)

    def keys(self):
        return self._distribution.keys()

    def items(self):
        return self._distribution.items()

    def values(self):
        return self._distribution.values()

    def get(self, key: K, default=None):
        return self._distribution.get(key, default)

