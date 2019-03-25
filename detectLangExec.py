# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 12:03:41 2019

@author: user
"""
import time 
import  pymongo
from pymongo import MongoClient
import pprint
from pymongo import MongoClient
import detectlangmethodsbackup as dlmb

#pmName = input('Enter module name:')
#dlmb = __import__(pmName)
#print(dir(dlmb))

client = MongoClient("mongodb://localhost:27017/facebook")
db = client.facebook
fb = db.fb 
#print('Total Record for the collection: ' + str(fb.count()))
postsArray = ['']
for record in fb.find().limit(10):
    value = record["message"]
    #postsArray = postsArray.append(value)
    lang=dlmb.detectPlusTranslate(value)
    print(dlmb.detectPlusTranslate(value))
    fblang = db.fblang 
    data = {"post": value,
            "language":lang }
    word_id = fblang.insert_one(data).inserted_id
    #pprint.pprint(value)
    
     