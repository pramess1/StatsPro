import unittest
from sys import path
path.append("../src")
import stats

class StatsTests(unittest.TestCase):
    
    def test_total_numbers(self):
        total = stats.total_numbers(2, 20, 11)
        self.assertEqual(total, 33)

    def test_total_list(self):
        total = stats.total_list([2, 5, 81])
        self.assertEqual(total, 88)

    def test_total_dict(self):
        total = stats.total_dict({2: 4, 5: 6 })
        self.assertEqual(total, 10)

    def test_average_numbers(self):
        self.assertEqual(stats.average_numbers(10, 20, 15), 15)

    def test_average_list(self):
        to_average = [2, 4, 6, 8, 10]
        self.assertEqual(stats.average_list(to_average), 6)

    def test_average_dict(self):
        to_average = {1: 2, 3: 4, 5: 6}
        self.assertEqual(stats.average_dict(to_average), 4)