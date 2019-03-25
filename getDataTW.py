# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 15:53:36 2019

@author: user
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 15:48:16 2019

@author: user
"""

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
client = MongoClient('mongodb://192.168.1.104:27017/')


#collection = db.get_data


#clientInfo = db.clientInfo

keyWordClient = []
idClient = []
postsArray = []


def findPost(database,collectionC,collectionP):

    for record in collectionC.find().limit(10):
         #print("test")
         valueId = record["id"]
         idClient.append(valueId)
         valueKeyW = record["key_words"]
         keyWordClient.append(valueKeyW)
         
    #print(idClient)     
    #print(keyWordClient)

    j = 0
    for record in collectionP.find().limit(10):
         #print(record)
         value = record["message"]
         #postsArray.append(value)
         #pprint.pprint(value)
         for wordlist in keyWordClient :
             idCli = collectionC.find({"key_words":wordlist})  
             get_dataTW = db.get_dataTW
             
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
                     get_dataTW.insert_one(data)
                     j += 1 
                 else : 
                     exit
                     
db = client.twitter
collectionPost = db.tw
collectionClient = db.clientInfo
print(findPost(db,collectionClient,collectionPost))

end = time.time()
print(end-start)