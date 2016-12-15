import spacy
import pymongo

nl = spacy.load("en")
client = pymongo.MongoClient()
dbs = client.test
main_dict = {}
lists = []
def nlpspace():
    output= ""
    #HTML_text = dbs.cahn.distinct("HTML_text")
    
    r = open("rawhtml.txt","r")
    HTML_text = r.read()
    
    para = nl.make_doc(HTML_text)
    
    #parsedpara = nl.pipeline(para)
    
    for token in para:
        token = str(token)
        token.replace(" ", "")
        if token != "\n":
    
            lists.append(token)
        
    main_dict["Dictionary"] = lists
    
    dbs.dict.insert_one(main_dict)
        
    r.close()
        
nlpspace()