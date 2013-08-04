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
        round_errors = {}
        round_scores = {}

    """Adds a score for a round.

    Adds a score from a given round to the round scores dictionary.

    Args:
        round_number: Number of the round for the inputted score.
        round_score: Score of the inputted round.
        round_errors: Errors of the inputted round.
    """
    def add_round(self, round_number, round_score, round_errors):
        round_num = round_number
        round_scores[round_num] = round_score
        round_errors[round_num] = round_errors

    """Deletes a given round.

    Subtracts the score and errors of the given round.

    Args:
        round_index: The index of the round to be deleted
    """
    def delete_round(self, round_index):
        if round_scores[round_index] == "undefined" or round_errors[round_index] == "undefined":
            return "Please pick a score from an already inputted round."
        else:
            # remove value from round_scores list and subtract it from total
            # score
            del round_scores[round_index]
            del round_errors[round_index]
            print "Round " + (round_index + 1) "'s score has been deleted."
            return

    """Calculates the score for the individual.

    Calculates the total number of points accumulated by an individual.

    Returns: The total score of the individual.
    """
    def get_score(self):
        total = 0
        for score in round_scores:
            total += score
        return total

    """Calculates the average of each score.

    Calculates the average of the scores of the individual.
    
    Returns:
        Int: Average of the individuals scores.
    """
    def get_average(self):
        """ calculates the average of all scores """
        return self.get_score() / len(round_scores)
