"""Class for connecting to the mongodb. 

- Allows for inputting of rounds and players into a scalable mongodb database
- Allows for searching for rounds and persons
"""
import pymongo
import datetime

class pymongodb(object):
	def __init__(self, ):
		self.person
	    
	def connect_to_mongo():
	    client = MongoClient("localhost", 27017)
	    db = client.statpro

	def post_person():
		post = {"person"  : _person,
				"round"   : _round,
				"tags"	  : [_tag, _tag2]
				"date"    : _datetime
				}
		person = db.person
		person_pers = person.insert(person)

	def post_round():
		post = {"team"    : _team,
				"members" : _members
				"tags"	  : [_tag, _tag2]
				"date"    : _datetime
			    }
		round = db.round
		round_rond = round.insert(round)

	def search_person():
		person.find_one({"_pers": person_pers})

	def search_round():
		round.find_one({"_rond": round_rond})


