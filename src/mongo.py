"""Class for connecting to the mongodb.

- Allows for inputting of rounds and players into a scalable mongodb database
- Allows for searching for rounds and persons
"""
import pymongo
import datetime

class pymongodb(object):
    def __init__(self):
    	self.database
        self.person
        self.round_

    def connect_to_mongo(self):
        client = MongoClient("localhost", 27017)
        database = client.statpro

    def post_person(self, person, round_, *tags, date):
        post = {"person"  : person,
                "round"   : round_,
                "tags"    : tags
                "date"    : date
                }
        person = database.person
        person_pers = person.insert(person)

    def post_round(self):
        post = {"team"    : team,
                "members" : members
                "tags"    : tags
                "date"    : datetime
                }
        self.round_ = database.round_
        round_rond = self.round_.insert(round)

    def search_person(self):
        person.find_one({"person": person_pers})

    def search_round(self):
        round_.find_one({"round": round_rond})
