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

"""Creates a new person.

Allows for the creation and manipulation of a person and his
score.
"""

class Person(object):

    def __init__(self):
        self.round_errors = {}
        self.round_scores = {}

    def get_round_score(self, _round):
        return self.round_scores[_round]

    def get_total_score(self):
        total = 0
        for score in self.round_scores:
            total += self.round_scores[score]
        return total

    """Adds a score to a round.
    Uses a dictionary to add a score to a round number.
    Args:
        Int     _round       The round number to add.
        Int     score        The score to be added.
    """
    def add_round_score(self, _round, score):
        self.round_scores[_round] = score

    def delete_round_score(self, _round):
        del(self.round_scores[_round])

    def get_round_errors(self, _round):
        return self.round_errors[_round]

    def get_total_errors(self):
        total = 0
        for error in self.round_errors:
            total += self.round_errors[error]
        return total

    def add_round_errors(self, _round, errors):
        self.round_errors[_round] = errors

    def delete_round_errors(self, _round):
        del(self.round_errors[_round])