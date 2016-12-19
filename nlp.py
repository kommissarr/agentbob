import spacy
import pymongo

nl = spacy.load("en")
client = pymongo.MongoClient()
dbs = client.sdb

text = dbs.another.find({"Page_tags":"smh"})
text = text.distinct("HTML_text")
def nlpspace():

    para = nl(text[0])
    nl.ents = []
    for token in para.sents:
        for entities in para.ents:
            
            print(entities, entities.label_)

        
nlpspace()