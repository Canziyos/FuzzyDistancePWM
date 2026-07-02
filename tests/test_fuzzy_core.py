import unittest

from fuzz.fuzzy_core import FuzzyCore
from fuzz.fuzzy_config import input_sets, output_sets, output_ranges, rules


class TestFuzzyCore(unittest.TestCase):
    def test_distance_1000_returns_valid_pwm_outputs(self):
        controller = FuzzyCore(input_sets, output_sets, rules, output_ranges)

        result = controller.compute({"distance": 1000})

        self.assertIn("duty", result)
        self.assertIn("freq", result)
        self.assertGreaterEqual(result["duty"], 0)
        self.assertLessEqual(result["duty"], 100)
        self.assertGreaterEqual(result["freq"], 100)
        self.assertLessEqual(result["freq"], 2000)


if __name__ == "__main__":
    unittest.main()
