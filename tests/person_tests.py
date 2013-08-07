"""
Copyright (c) 2013 Daniel Seymour All rights reserved

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

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

    def test_get_round_score(self):
        self.dummy.add_round_score(1, 20)
        self.assertEqual(self.dummy.get_round_score(1), 20)

    def test_get_total_score(self):
        self.dummy.add_round_score(1,30)
        self.dummy.add_round_score(2,40)
        self.assertEqual(self.dummy.get_total_score(), 70)

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

    def test_get_round_errors(self):
        self.dummy.add_round_errors(1, 2)
        self.assertEqual(self.dummy.get_round_errors(1), 2)

    def test_get_total_errors(self):
        self.dummy.add_round_errors(1, 3)
        self.dummy.add_round_errors(2, 4)
        self.assertEqual(self.dummy.get_total_errors(), 7)
    
    def test_add_round_errors(self):
        self.dummy.add_round_errors(1, 2)
        self.assertEqual(self.dummy.round_errors, {1: 2})

    def test_delete_round_errors(self):
        self.dummy.add_round_errors(1, 3)
        self.dummy.add_round_errors(2, 4)
        self.dummy.delete_round_errors(2)
        self.assertEqual(self.dummy.round_errors, {1: 3})