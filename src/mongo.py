"""
Copyright (c) 2013 William Fleming All rights reserved

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


