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


class team:

    def __init__(self, team_name, number_members):
        name = team_name
        members = []
        round_ = {}
        total_points = []
    
    def set_team_name(self, name):
        if name == "undefined" or name == None:
            return "Please enter a valid name."
        else:
            self.name = name
            return "Name set!"

    def get_team_name():
        return self.name

    def set_team_members(self, *args):
        if len(args) > 5:
            return "Teams can only have 5 members."
        else:
            for member in args:
                members.append(member)
            return "Team members added."    

    def get_team_members(self):
        if len(members) == 0:
            return "This team has no members."
        else:
            return members

