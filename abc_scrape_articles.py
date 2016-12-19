import pymongo
import scrape_agent
import datetime

bob = scrape_agent.scrape("bob")
website = "http://www.abc.net.au/news/2016-11-29/malaysian-pm-najib-razak-voices-support-for-islamic-laws-as-he-/8076766"
template = {}
temphtml = "rawhtml.txt"
def nlpspace():
    print (bob.name + " is working hard on " + website)
    bob.htmlpull(website,temphtml)
    #linkscraper() returns a tuple : tuple(0) is the actual list of links
    # tuple (1) is the tag association with the links
    listoflinks = bob.linkscraper(temphtml,website)

    page_tag = listoflinks[1]
    listoflinks = listoflinks[0]

    txt = bob.abchtmlsanitize(temphtml)
    page_title = txt[2]
    publishtime = txt[1]
    txt = txt[0]
    #dbs.cahn.ensure_index("Associated_links")
    
    template["Associated_links"] = listoflinks
    template["HTML_text"] = txt
    template["Page_tags"] = page_tag
    template["URL"] = website
    template["Scrape_time"] = datetime.datetime.today()
    template["Publish_time"] = publishtime
    template["Page_title"] = page_title

    print (txt)
    print (publishtime)
    print (page_title)
        
nlpspace()