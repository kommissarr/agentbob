import re
import scrape_agent
import datetime
from pymongo import MongoClient

__name__ = "__scraper__"
bob = scrape_agent.scrape("bob")
website = "https://www.bloomberg.com/news/articles/2016-12-14/gold-languishes-as-fed-chief-yellen-expected-to-pull-the-trigger" 
template = {}
client = MongoClient()
database_name = "sdb"
dbs = client[database_name]
collection_name = 'another'

temphtml = "rawhtml.txt"

print ("Writing to database: " + dbs.name)
print (bob.name + " is working hard on " + website)
bob.htmlpull(website,temphtml)

listoflinks = bob.linkscraper(temphtml,website)

collcount = dbs[collection_name].count()
# for words in mongoread:
#     print (words)
txt = bob.htmlsanitize(temphtml)

#dbs.cahn.ensure_index("Associated_links")
template["Associated_links"] = listoflinks
template["HTML_text"] = txt
template["URL:"] = website
template["Time:"] = str(datetime.datetime.today())

#print (template)

dbs[collection_name].update(template,{})
print ("There are currently " + str(collcount) + "  documents in collection: " + dbs[collection_name].name)
client.close()