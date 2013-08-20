"""Class for connecting to the mongodb.

- Allows for inputting of rounds and players into a scalable mongodb database
- Allows for searching for rounds and persons
"""
import pymongo
import datetime

class MongoDB(object):
    def __init__(self):
    	self.database
        self.person
        self.round_
        self.date = datetime.date.today()

    def connect_to_mongo_database(self):
        client = MongoClient("localhost", 27017)
        self.database = client.StatsPro

    def initial_post_person(self, person, round_):
        post = {"person"  : person,
                "round"   : round_,
                "date"    : datetime.date.today()
                }
        self.person = database.person
        person_pers = person.insert(person)

    def initial_post_team(self, team, round_):
        post = {"team"    : team,
                "members" : members,
                "date"    : datetime.date.today()
                }
        self.round_ = database.round_
        round_rond = self.round_.insert(round_)

    def search_person(self, name):
        person.find_one({"person": name})

    def search_round(self, number):
        round_.find_one({"round": number})
