from typing import Dict
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

    def __init__(
        self,
        distribution: Dict[A, StateProbabilityDistribution[SI]]
    ) -> None:
        super().__init__(
            distribution=distribution
        )

    # TODO See if the error checking can be done in super()
    def set_distribution(
        self,
        distribution: Dict[A, StateProbabilityDistribution[SI]]
    ) -> None:
        if not distribution:
            raise ValueError(f"Empty probability distribution provided for {self.__class__.__name__}.")

        self.clear()
        self.update(distribution.copy())

    def set_distribution_for_key(
        self,
        key: A,
        distribution: StateProbabilityDistribution[SI]
    ) -> None:
        if not key in self.keys():
            raise KeyError(f"State Index {key} not within {self.__class__.__name__}.")

        self[key] = distribution

    def get_distribution(self) -> Dict[A, StateProbabilityDistribution[SI]]:
        pass

    def get_distribution_of_key(
        self,
        key: A
    ) -> StateProbabilityDistribution[SI]:
        pass
