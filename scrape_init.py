import re
import scrape_agent

__name__ = "__scraper__"
bob = scrape_agent.scrape("bob")
website = "http://www.smh.com.au/nsw/digitaleditionredirector" 


temphtml = "rawhtml.txt"
textcontent = "textcontent.txt"

print (bob.name + " is working hard on " + website)
bob.htmlpull(website,temphtml)
bob.linkscraper(temphtml,website)
bob.htmlsanitize(temphtml, textcontent)