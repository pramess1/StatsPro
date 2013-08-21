"""Creates a new person.

Allows for the creation and manipulation of a person and his
score.
"""

class Person(object):

    def __init__(self):
        self.name = ""
        self.round = {}

    def get_person_name(self):
        return self._name

    def set_person_name(self, name):
        self._name = name

    def add_round(self, round_, score, errors):
        if is_win == True:
            self._round[round_] = [score, errors]
        else:
            self._round[round_] = [score, errors]

    def delete_round(self, round_):
        del self._round[round_]

    def get_round(self, round_):
        return self._round[round_]

    def change_round_score(self, round_, new_score):
        self._round[round_][0] = new_score

    def change_round_errors(self, round_, new_errors):
        self._round[round_][1] = new_errors

    def get_round_score(self, round_):
        return self._round[round_][0]

    def get_round_errors(self, round_):
        return self._round[round_][1]
