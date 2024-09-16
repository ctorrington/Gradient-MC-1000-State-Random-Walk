import unittest

from typing import Dict

from tests.utils import timed
from core.dependency.action import Action
from core.dependency.state_index import StateIndex
from core.dependency.state_probability_distribution_new import StateProbabilityDistribution
from core.dependency.state_actions_new import StateActions

class TestStateActionsNew(unittest.TestCase):
    @timed
    def test_init(self):
        index_distribution: Dict[int, float] = {
            1: 0.3,
            2: 0.4,
            3: 0.3
        }
        state_distribution: StateProbabilityDistribution[int] = (
            StateProbabilityDistribution(
                distribution=index_distribution
            )
        )

        class TestActions(Action):
            ACTION1 = "action1"
            ACTION2 = "action2"
            ACTION3 = "action3"

        state_actions_distribution: Dict[Action, StateProbabilityDistribution[int]] = {
            TestActions.ACTION1: state_distribution,
            TestActions.ACTION2: state_distribution,
            TestActions.ACTION3: state_distribution
        }

        StateActions(
            distribution=state_actions_distribution
        )




if __name__ == "__main__":
    unittest.main()