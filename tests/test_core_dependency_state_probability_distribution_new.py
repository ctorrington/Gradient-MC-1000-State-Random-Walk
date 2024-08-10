import unittest

from typing import Any

from tests.utils import timed
from core.dependency.state_probability_distribution_new import StateProbabilityDistribution

class TestStateProbabilityDistributionNew(unittest.TestCase):
    @timed
    def test_init_with_int_index(self):
        index1: int = 1
        index2: int = 2

        prob_distro_int: dict[Any, float] = {
            index1: 0.2,
            index2: 0.03
        }

        state_prob_init = StateProbabilityDistribution(
            distribution=prob_distro_int
        )
        
        self.assertEqual(prob_distro_int, state_prob_init)

    @timed
    def test_init_with_tuple_int_index(self):
        index_1_tuple = (0, 1)
        index_2_tuple = (0, 2)
        
        prob_distro_tuple_int = {
            index_1_tuple: 0.1,
            index_2_tuple: 0.2,
        }
        
        state_prob_tuple = StateProbabilityDistribution(
            distribution=prob_distro_tuple_int
        )
        
        self.assertEqual(prob_distro_tuple_int, state_prob_tuple)

    @timed
    def test_set_probability_for_key(self):
        int_index_prob_distro = StateProbabilityDistribution(
            distribution={
                1: 0.2,
                2: 0.03
            }
        )

        key = 1
        prob_value = 0.7
        int_index_prob_distro.set_distribution_for_key(
            key=key,
            distribution=prob_value
        )
        self.assertEqual(int_index_prob_distro[key], prob_value)

    @timed
    def test_set_probability_for_invalid_key(self):
        index1: int = 1
        index2: int = 2
        prob_distro_int: dict[Any, float] = {
            index1: 0.2,
            index2: 0.03
        }
        int_index_prob_distro = StateProbabilityDistribution(
            distribution=prob_distro_int
        )

        with self.assertRaises(KeyError):
            int_index_prob_distro.set_distribution_for_key(
                key=9000,
                distribution=1
            )

    @timed
    def test_set_probability_for_empty_key(self):
        index1: int = 1
        index2: int = 2
        prob_distro_int: dict[Any, float] = {
            index1: 0.2,
            index2: 0.03
        }
        int_index_prob_distro = StateProbabilityDistribution(
            distribution=prob_distro_int
        )

        with self.assertRaises(KeyError):
            int_index_prob_distro.set_distribution_for_key(
                key="",
                distribution=1
            )

    @timed
    def test_set_probability_distribution(self):
        index1: int = 1
        index2: int = 2
        prob_distro_int: dict[Any, float] = {
            index1: 0.2,
            index2: 0.03
        }
        int_index_prob_distro = StateProbabilityDistribution(
            distribution=prob_distro_int
        )

        distro = {
            1: 5.0,
            2: 6.0,
            3: 7.0,
            4: 8.0,
            5: 9.0
        }
        int_index_prob_distro.set_distribution(distro)
        
        self.assertEqual(distro, int_index_prob_distro)

    @timed
    def test_set_probability_empty_distribution(self):
        index1: int = 1
        index2: int = 2
        prob_distro_int: dict[Any, float] = {
            index1: 0.2,
            index2: 0.03
        }
        int_index_prob_distro = StateProbabilityDistribution(
            distribution=prob_distro_int
        )

        distro: dict[int, float] = {}
        
        with self.assertRaises(ValueError):
            int_index_prob_distro.set_distribution(distro)

    @timed
    def test_get_probability_of_key(self):
        key = 1
        probability = 1.0
        
        test_distro = StateProbabilityDistribution(
            distribution={key: probability}
        )
        
        self.assertEqual(
            probability, test_distro.get_distribution_of_key(key=key)
        )

    @timed
    def test_get_probability_of_invalid_key(self):
        key = 1
        invalid_key = 5
        probability = 1.0
        
        test_distro = StateProbabilityDistribution(
            distribution={key: probability}
        )
        
        with self.assertRaises(KeyError):
            test_distro.get_distribution_of_key(invalid_key)

if __name__ == "__main__":
    unittest.main()