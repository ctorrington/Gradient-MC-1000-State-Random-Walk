import unittest

from tests.utils import timed
from typing import Any

from core.dependency.state_probability_distribution import StateProbabilityDistributionNew

class TestStateProbabilityDistribution(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)

        # Int test data.
        index1: int = 1
        index2: int = 2
        index3: int = 3
        index4: int = 4
        index5: int = 5

        self.prob_distro_int: dict[Any, float] = {
            index1: 0.2,
            index2: 0.03,
            index3: 0.5,
            index4: 0.2,
            index5: 0.07
        }
        
        # Tuple test data.
        index_1_tuple = (0, 1)
        index_2_tuple = (0, 2)
        index_3_tuple = (1, 0)
        index_4_tuple = (2, 0)
        index_5_tuple = (1, 1)
        index_6_tuple = (2, 2)
        
        self.prob_distro_tuple_int = {
            index_1_tuple: 0.1,
            index_2_tuple: 0.2,
            index_3_tuple: 0.3,
            index_4_tuple: 0.2,
            index_5_tuple: 0.1,
            index_6_tuple: 0.1
        }

    @timed
    def test_init_with_int_index(self):
        self.int_index_prob_distro = StateProbabilityDistributionNew(
            probability_distribution=self.prob_distro_int
        )

    @timed
    def test_init_with_tuple_int_index(self):
        StateProbabilityDistributionNew(
            probability_distribution=self.prob_distro_tuple_int
        )

    @timed
    def test_set_probability_for_key(self):
        key = 1
        prob_value = 0.7
        self.int_index_prob_distro.set_probability_for_key(
            key=key,
            probability=prob_value
        )
        self.assertEqual(self.int_index_prob_distro[key], prob_value)

    @timed
    def test_set_probability_for_invalid_key(self):
        with self.assertRaises(KeyError):
            self.int_index_prob_distro.set_probability_for_key(
                key=9000,
                probability=1
            )

    @timed
    def test_set_probability_for_empty_key(self):
        with self.assertRaises(KeyError):
            self.int_index_prob_distro.set_probability_for_key(
                key="",
                probability=1
            )

    @timed
    def test_set_probability_distribution(self):
        distro = {
            1: 5.0,
            2: 6.0,
            3: 7.0,
            4: 8.0,
            5: 9.0
        }
        self.assertEqual(distro, self.int_index_prob_distro.set_probability_distribution(distro))

    @timed
    def test_set_probability_empty_distribution(self):
        distro: dict[int, float] = {}
        
        with self.assertRaises(ValueError):
            self.int_index_prob_distro.set_probability_distribution(distro)

    @timed
    def test_get_probability_of_key(self):
        key = 1
        probability = 1.0
        
        test_distro = StateProbabilityDistributionNew(
            probability_distribution={key: probability}
        )
        
        self.assertEqual(probability, test_distro.get_probability_of_key(key=key))

    @timed
    def test_get_probability_of_invalid_key(self):
        key = 1
        invalid_key = 5
        probability = 1.0
        
        test_distro = StateProbabilityDistributionNew(
            probability_distribution={key: probability}
        )
        
        with self.assertRaises(KeyError):
            test_distro.get_probability_of_key(invalid_key)

if __name__ == "__main__":
    unittest.main()
