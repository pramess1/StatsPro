"""Creates a Team

Creates a class called team that will be used to create a manipulate teams in plugins.
"""
class Team(object):

    def __init__(self):
        self._name = ""
        self._round = {}
        self._team_members = []
        self._opposing_team = {}
        self._team_scores = {}
        self._team_wins_losses_round = {}

    """Returns the name of the team.
    Returns the name of the team.
    Returns:
        String: the name of the team as a string.
    """
    def get_team_name(self):
        return self._name

    """Sets the name of the team.
    Simply sets the name of the team.
    Args:
        String: the name of the team as a string.
    """
    def set_team_name(self, name):
        self._name = name

    """Adds a round to the team.
    Adds a round with all data to the current team.
    Args:
        Integer: the round number
        Integer: the round score
        String: the name of the opposing team
        Boolean: whether the round was a win or loss
    """
    def add_round(self, round_, score, errors, opponent, is_win):
        if is_win == True:
            self._round[round_] = [score, errors, opponent, "W"]
        else:
            self._round[round_] = [score, errors, opponent, "L"]

    """Removes a round from the current team.
    Removes a round and all data from the current team.
    Args:
        Integer: the round number to delete.
    """
    def delete_round(self, round_):
        del self._round[round_]

    """Gets a round.
    Returns a round that is passed to the function.
    Args:
        round_: integer
    """
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
