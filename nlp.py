import spacy
import pymongo

nl = spacy.load("en")
client = pymongo.MongoClient()
dbs = client.sdb

text = dbs.another.distinct("HTML_text")
def nlpspace():
    
    print (text)
    para = nl.make_doc(text[0])
    
    for token in para:
        print(token)

        
nlpspace()