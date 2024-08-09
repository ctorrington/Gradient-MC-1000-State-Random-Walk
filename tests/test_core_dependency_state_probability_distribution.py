import unittest

from tests.utils import timed

from core.dependency.state_probability_distribution import StateProbabilityDistributionNew

class TestStateProbabilityDistribution(unittest.TestCase):

    @timed
    def test_init(self):
        index1: int = 1
        index2: int = 2
        index3: int = 3
        index4: int = 4
        index5: int = 5
    
        prob_distro: dict[int, float] = {
            index1: 0.2,
            index2: 0.03,
            index3: 0.5,
            index4: 0.2,
            index5: 0.07
        }

        StateProbabilityDistributionNew(
            probability_distribution=prob_distro
        )

if __name__ == "__main__":
    unittest.main()
