import unittest
import sys
sys.path.append("../src")
import person

class PersonTests(unittest.TestCase):

    def setUp(self):
        self.dummy = person.Person()  

    def test_person_exists(self):
        dummy_type = type(self.dummy)
        self.assertIs(dummy_type, person.Person)

    def test_score_exists(self):
        dummy_score = self.dummy.round_scores
        self.assertIsInstance(dummy_score, dict)

    def test_add_round_score(self):
        self.dummy.add_round_score(1, 20)
        self.assertEqual(self.dummy.round_scores, {1: 20})

    def test_delete_round_score(self):
        self.dummy.add_round_score(1, 90)
        self.dummy.add_round_score(2, 20)
        self.dummy.delete_round_score(1)
        self.assertEqual(self.dummy.round_scores, {2: 20})
    
    def test_errors_exists(self):
        dummy_errors = self.dummy.round_errors
        self.assertIsInstance(dummy_errors, dict)

    def test_add_round_errors(self):
        self.dummy.add_round_errors(1, 2)
        self.assertEqual(self.dummy.round_errors, {1: 2})

    def test_delete_round_errors(self):
        self.dummy.add_round_errors(1, 3)
        self.dummy.add_round_errors(2, 4)
        self.dummy.delete_round_errors(2)
        self.assertEqual(self.dummy.round_errors, {1: 3})