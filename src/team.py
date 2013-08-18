"""Creates a Team

Creates a class called team that will be used to create a manipulate teams in plugins.
"""
class Team(object):

    def __init__(self):
        self._name = ""
        self._team_members = []
        self._opposing_team = {}

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

    """Gets the team_members of the team
    Gets the team members and returns a list
    Returns:
        List: a list of all the members on a team.
    """
    def get_team_members(self):
        return self._team_members

    """Adds a team member.
    Adds an indefinite number of members to a team.
    Args:
        Strings: any number of strings
    """
    def add_team_members(self, *names):
        for member in names:
            self._team_members.append(member)

    """Gets the members of a team.
    Gets all of the members of the team.
    Returns:
        List: a list of team members in any type.
    """
    def get_team_members(self):
        return self._team_members

    """Sets the name of the opposing team.
    Sets the name of the opposing team for a certain round.
    """
    def set_opposing_team(self, round_, team):
        self._opposing_team[round_] = team

    """Gets the name of the oppsiing team.
    Gets the name of the opposing team for a certain round.
    Returns:
        String: the name of the opposing team
    """
    def get_opposing_team(self, round_):
        return self._opposing_team[round_]
