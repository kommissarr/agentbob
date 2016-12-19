from textblob import TextBlob
import pymongo
client = pymongo.MongoClient()
dbs = client.sdb
text = dbs.another.find({"Page_tags":"smh"})
text = text.distinct("HTML_text")
blob = TextBlob(text[0])

# for all in blob.noun_phrases:
#     print(all)


for sent in blob.sentences:
    print (sent)
    print (sent.sentiment)

print (blob.sentiment)