"""Creates a Team

Creates a class called team that will be used to create a manipulate teams in plugins.
"""
class Team(object):

    def __init__(self):
        self._name = ""
        self._team_members = []

    """Returns the name of the team.
    Returns the name of the team.
    Returns:
        String:    The name of the team as a string.
    """
    def get_team_name(self):
        return self._name

    """Sets the name of the team.
    Simply sets the name of the team.
    Args:
        String:    The name of the team as a string.
    """
    def set_team_name(self, name):
        self._name = name

    """Gets the team_members of the team
    Gets the team members and returns a list
    Returns:
        List:    A list of all the members on a team.
    """
    def get_team_members(self):
        return self._team_members

    """Adds a team member.
    Adds an indefinite number of members to a team.
    Args:
        Any:    Will take any input type.
    """
    def add_team_members(self, *names):
        for member in names:
            self._team_members.append(member)

    """Gets the members of a team.
    Tets all of the members of the team.
    Returns:
        List:    A list of team members in any type.
    """
    def get_team_members(self):
        return self._team_members