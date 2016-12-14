import spacy
import pymongo

nl = spacy.load("en")
client = pymongo.MongoClient()
dbs = client.test
main_dict = {}
def nlpspace():
    output= ""
    #HTML_text = dbs.cahn.distinct("HTML_text")
    
    r = open("rawhtml.txt","r")
    HTML_text = r.read()
    
    para = nl.make_doc(HTML_text)
    
    #parsedpara = nl.pipeline(para)
    
    for token in para:
        str(token)

        main_dict[token] = token

    w = open("dict.txt", "w")
    dbs.dict.insert_one(main_dict)

        
nlpspace()