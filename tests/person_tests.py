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

    def test_name_exists(self):
        self.assertIs(self.dummy.name, "")

    