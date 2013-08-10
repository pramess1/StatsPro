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

    def test_get_team_members(self):
        self.dummy._team_members = ["Daniel", "Anna"]
        self.assertEqual(self.dummy.get_team_members(), ["Daniel", "Anna"])

    def test_add_team_member(self):
        self.dummy.add_team_members("Daniel")
        self.dummy.add_team_members("Anna", "Heather", "Kimberly")
        self.assertListEqual(self.dummy.get_team_members(), ["Daniel", "Anna", "Heather", "Kimberly"])