import html2text
import urllib
import re
from bs4 import BeautifulSoup


class scrape:

    name = ""

    website = ""
    tempfile = ""
    regex = "^\/[a]"
    def __init__(self,name):
       self.name = name

    
    def htmlpull(self, website, tempfile):
        
        pagedata = urllib.request.urlopen(website)
        #fullhtml is the stored text of the HTTP object
        fullhtml = pagedata.read() 
        #Request status
        HTTPstatus = pagedata.getcode()
        #Temp file for later processing
        
        if HTTPstatus != 200:
            goodtogo = "Request not successful"
        else:
            goodtogo = "Request is successful"
            
            temphtml = open(tempfile,"wb")
            temphtml.write(fullhtml)
            temphtml.close()
            pagedata.close()
        print ("HTTP status code:", HTTPstatus, goodtogo, "\nTemp file location ",tempfile)

    #pulls text from htmlfiles
    def htmlsanitize(self, tempfile, outfile):
        
        temphtml = tempfile
        print ("HTMLParsing/Sanitizing raw html data...")
        #opens temp file 
        htmlfile = open(temphtml, "r", 1)
        # inserts into new txt file
        sanitizedfile = open(outfile, "w")
        txt = htmlfile.read()
        #get rid of scripts and headers of the raw html data
        txt = html2text.html2text(txt, "utf-8")
        #writes sanitized text into a new temp file 
        sanitizedfile.write(txt)
        # close files
        htmlfile.close()
        sanitizedfile.close()



    #rawfile is the rawhtml txt file
    #website is the rootwebsite to be appended to if the scraped link is relative
    def linkscraper(self, rawfile, website):
        tag = website.split(sep=".")
        tag.remove(tag[0])
        
        
        print("Scraping for a href links with urls containing: " + tag[0])
        listoflinks = []
        otherlinks =[]
        listdict = {}
        #open file for writing
        temphtml = open(rawfile, "r")
        #converts temphtml markup to text (soup)
        text = BeautifulSoup(temphtml, "lxml")
        
        #SPECIAL REGEX FOR CLASSIFYING FILE NAMES WITH TAGS : links_% + tag 
        linkfilename = "links_%" + tag[0] + "--.txt"
        #opens writing file 
        linkfile = open(linkfilename, "w")

        #insert all links into $linkfilename starting with http
        for link in text.find_all("a"):
            links = link.get('href')

            #avoid scraping duplicate links
            if links in listoflinks or links in otherlinks:
                continue
            #link must be in string format
            if type(links) == str:
                #check the root of the URL
                netloc = urllib.parse.urlparse(links).netloc    
                #if no root URL shown meaning the a href is relative, and needs to be appended to the end of the root website ie. www.fool.com
                if netloc == "": 
                    joinedlinks = urllib.parse.urljoin(website, links)
                    listoflinks.append(joinedlinks)
                                           
                #if the link is associated with the root website or its tags derived from keywords in the URL
                if tag[0] in netloc:
                    listoflinks.append(links)
                
        
        #Add to dictionary to be inserted into mongodb 
        listdict["Associated links"] = listoflinks
        #listdict["Non-associated links"] = otherlinks            
        
        print ("Number of associated links on page: " + str(len(listoflinks)))             
        
        #writes listoflinks into txt file to be crawled later on
        
        # for ele in range(0, len(listoflinks)):
        #     linkfile.write(listoflinks[ele])
        #     linkfile.write("\n")
        temphtml.close()
        linkfile.close()         
        return listdict
    
