import unittest
import sys
sys.path.append("../src")
import team

class TeamTests(unittest.TestCase):

    def setUp(self):
        self.dummy = team.Team()

    def test_team_exists(self):
        dummy_type = type(self.dummy)
        self.assertIs(dummy_type, team.Team)

    def test_get_team_name(self):
        self.dummy._name = "La Grande"
        self.assertEqual(self.dummy.get_team_name(), "La Grande")

    def test_set_team_name(self):
        self.dummy.set_team_name("baker city")
        self.assertEqual(self.dummy._name, "baker city")

    def test_add_round(self):
        self.dummy.add_round(1, 210, 6, "La Grande", True)
        self.assertEqual(self.dummy._round, {1: [210, 6, "La Grande", "W"]})

    def test_delete_round(self):
        self.dummy.add_round(1, 210, 6, "Baker City", False)
        self.dummy.add_round(2, 100, 4, "La Grande", True)
        self.dummy.delete_round(2)
        self.assertEqual(self.dummy._round, {1: [210, 6, "Baker City", "L"]})

    def test_get_round(self):
        self.dummy.add_round(1, 120, 3, "Baker City", False)
        self.assertEqual(self.dummy.get_round(1), [120, 3, "Baker City", "L"])

    def test_change_round_score(self):
        self.dummy.add_round(1, 120, 3, "Baker City", False)
        self.dummy.change_round_score(1, 200)
        self.assertEqual(self.dummy.get_round(1), [200, 3, "Baker City", "L"])

    def test_change_round_errors(self):
        self.dummy.add_round(1, 120, 3, "Baker City", False)
        self.dummy.change_round_errors(1, 5)
        self.assertEqual(self.dummy.get_round(1), [120, 5, "Baker City", "L"])

    def test_change_round_opponent(self):
        self.dummy.add_round(1, 120, 3, "Baker City", False)
        self.dummy.change_round_opponent(1, "LA")
        self.assertEqual(self.dummy.get_round(1), [120, 3, "LA", "L"])

    def test_change_round_record(self):
        self.dummy.add_round(1, 120, 3, "Baker City", False)
        self.dummy.change_round_record(1, True)
        self.assertEqual(self.dummy.get_round(1), [120, 3, "Baker City", "W"])
