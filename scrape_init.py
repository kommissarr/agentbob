import re
import scrape_agent
import datetime
from pymongo import MongoClient

__name__ = "__scraper__"
bob = scrape_agent.scrape("bob")
website = "http://search.abc.net.au/s/search.html?query=commonwealth+bank+reports&collection=news_meta&form=simple&gscope1=10&start_rank="
template = {}
client = MongoClient()
database_name = "sdb"
dbs = client[database_name]
collection_name = 'abccba'
num_pages = 267
temphtml = "rawhtml.txt"
count = 0
current_website = 0
links = []
#w = open("abclinks.txt", "w")
while count != num_pages:
    current_website = count*10 + 11
    nwebsite = website + str(current_website)

    print (count)
    if count == num_pages:
        break
    print ("Writing to database: " + dbs.name)
    print (bob.name + " is working hard on " + nwebsite)
    bob.htmlpull(nwebsite,temphtml)
    #linkscraper() returns a tuple : tuple(0) is the actual list of links
    # tuple (1) is the tag association with the links
    listoflinks = bob.abclinkscraper(temphtml,nwebsite)

    page_tag = listoflinks[1]
    links = links + listoflinks[0]
    collcount = dbs[collection_name].count()


    txt = bob.htmlsanitize(temphtml)
    page_title = txt[2]
    publishtime = txt[1]
    txt = txt[0]
    

    print (listoflinks)

    #dbs[collection_name].replace_one({"Page_tags" : page_tag}, template)

    template["_id"] = str(count) +"_abc"
    template["HTML_text"] = txt
    template["Page_tags"] = page_tag
    template["URL"] = website
    template["Scrape_time"] = datetime.datetime.today()
    template["Publish_time"] = publishtime
    template["Page_title"] = page_title



    print ("There are currently " + str(collcount) + "  documents in collection: " + dbs[collection_name].name)
    print (nwebsite)
    count = count+1

template["Associated_links"] = links    
#dbs[collection_name].insert_one(template)    
client.close()