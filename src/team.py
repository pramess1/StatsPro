"""Creates a Team

Creates a class called team that will be used to create a manipulate teams in plugins.
"""
class Team(object):

    def __init__(self):
        self._name = ""
        self._round = {}

    def get_team_name(self):
        return self._name

    def set_team_name(self, name):
        self._name = name

    def add_round(self, round_, score, errors, opponent, is_win):
        if is_win == True:
            self._round[round_] = [score, errors, opponent, "W"]
        else:
            self._round[round_] = [score, errors, opponent, "L"]

    def delete_round(self, round_):
        del self._round[round_]

    def get_round(self, round_):
        return self._round[round_]

    def change_round_score(self, round_, new_score):
        self._round[round_][0] = new_score

    def change_round_errors(self, round_, new_errors):
        self._round[round_][1] = new_errors

    def change_round_opponent(self, round_, new_opponent):
        self._round[round_][2] = new_opponent

    def change_round_record(self, round_, new_record):
        if new_record == True:
            self._round[round_][3] = "W"
        else:
            self._round[round_][3] = "L"
