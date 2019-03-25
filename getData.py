# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 14:12:00 2019

@author: user
"""
import time 
import  pymongo
from pymongo import MongoClient
import pprint
from pymongo import MongoClient

start = time.time()
#client = MongoClient()
#client = MongoClient('localhost', 27017)
client = MongoClient('mongodb://localhost:27017/')

db = client.facebook
collection = db.get_data

fb = db.fb
clientInfo = db.clientInfo
#print('Total Record for the collection: ' + str(fb.count()))
#fruits.append("orange")
keyWordClient = []
idClient = []
postsArray = []
#print(postsArray)
#print("test")
#clientInfo.find().limit(10)
for record in clientInfo.find().limit(10):
     #print("test")
     valueId = record["id"]
     idClient.append(valueId)
     valueKeyW = record["key_words"]
     keyWordClient.append(valueKeyW)
     #pprint.pprint(valueKeyW)
     #pprint.pprint(valueId)

print(idClient)     
print(keyWordClient)

#print(fb.find("care"))
#print(fb.find({'message': {'$regex': 'care'}}))
#({},{ "_id": 0, "name": 1, "address": 1 }) ("")
"""
liste = clientInfo.find({ "_id": 0, "id": 0, "key_words": 1 })
print(liste)
for record in clientInfo.find({ "_id": 0, "id": 0, "key_words": 1 }) :
    print("yala raw3a")

    if fb.find({'message': {'$regex':record}}) == 0 :
        print(record["key_words"])
        print("found")
    else :
        exit
 
for c in clientInfo.find({"key_words":['care', 'clean', 'soft', 'soap', 'dove product', 'skin care']}):
    print(c["id"])
"""     
#print("what was the output")
j = 0
for record in fb.find().limit(10):
     #print(record)
     value = record["message"]
     #postsArray.append(value)
     #pprint.pprint(value)
     for wordlist in keyWordClient :
         idCli = clientInfo.find({"key_words":wordlist})  
         get_data = db.get_data
         
         #print(word_id)
         #print(idCli["id"])
         for word in wordlist :
             #print(fb.find({"message":word}))
             if word in value :
                 print(value)
                 
                 for c in idCli:
                     valId = c["id"]
                     print(c["id"])
                 #print(idCli)
                 data = {"Id": str(j),
                         "IdClient": valId,
                         "postLinkedToClient": value}
                 word_id = get_data.insert_one(data).inserted_id
                 j += 1 
             else : 
                 exit
     

end = time.time()
print(end-start)
print((((end-start)*1000000)/60)/60)