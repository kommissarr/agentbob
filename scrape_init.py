import re
import scrape_agent
import datetime
from pymongo import MongoClient

__name__ = "__scraper__"
bob = scrape_agent.scrape("bob")
website = "http://www.afr.com.au/" 

client = MongoClient()
dbs = client.test
coll = 'cahn'

print ("Writing to database: " + dbs.name)

temphtml = "rawhtml.txt"
textcontent = "textcontent.txt"

print (bob.name + " is working hard on " + website)
bob.htmlpull(website,temphtml)

listoflinks = bob.linkscraper(temphtml,website)
dbs.cahn.insert_one(listoflinks)
collcount = dbs.cahn.count()

print ("There are currently " + str(collcount) + "  documents in collection: " + dbs.cahn.name)
# for words in mongoread:
#     print (words)

bob.htmlsanitize(temphtml, textcontent)

