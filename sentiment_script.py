import os
from textblob import TextBlob
import  pymongo
from pymongo import MongoClient
import pprint
import requests
import time 
import langdetect 
from langdetect import detect
from langdetect import *
from textblob.translate import Translator

start = time.time()
client = MongoClient("mongodb://192.168.1.104:27017/testfacebook")
#db = client.facebook
#fb = db.fb
db = client.testfacebook
collectionPost = db.postshibapress
postsArray = []

for record in collectionPost.find().limit(100):
     value = record["message"]
     postsArray.append(value)
     #pprint.pprint(value)
     
#print(postsArray)

client = MongoClient("mongodb://192.168.1.104:27017/testfacebook")
db = client.testfacebook
sentiment = db.aa

def sentimentDefine(sentence):
    statsPositive=0
    statsNegative=0
    statsNeutral=0
    statsElse=0
    sentimentindicator = ""
    sentence = sentence.lower()
    sentence = TextBlob(sentence)
    #print(l.detect_language())
    if sentence.detect_language()  != "en" :
        #t = Translator()
        sentence = sentence.translate(to="en")
                
    sentence = sentence.lower()
    if  sentence.sentiment.polarity > 0 : 
        #print("Le poste '" + str(sentence) + "' est : positif")
        sentimentindicator = "positive"
        statsPositive+=1
    elif sentence.sentiment.polarity < 0 :
        #print("Le poste '" + str(sentence) + "' est : negatif")
        sentimentindicator = "negative"
        statsNegative+=1
    elif sentence.sentiment.polarity == 0 :
        #print("Le poste '" + str(sentence) + "' est : neutre")
        sentimentindicator = "neutral"
        statsNeutral+=1
    else :
        #print("Le poste '" + str(sentence) + "' est : sans sentiment")
        sentimentindicator = "none"
        statsElse+=1
                
            #post = {"message":str(l),
                    #"sentiment":sentimentindicator}
            #sentiment = db.sentiment
            #db.sentiment.insert_one(post)
            #print(word_id)        
            
    return sentimentindicator        
    
#print(sentimentDefine(postsArray))

for post in postsArray :
    print(post)
    if not post :
        print("Post is empty, sentiment can't be detected")
        sentimentindicator = "sentiment can't be detected"
    elif post == "null" :
        print("Post is empty, sentiment can't be detected")
        sentimentindicator = "sentiment can't be detected"
    else :
        print(post + " : " + sentimentDefine(post))
          
   
#print("Le nombre de poste positives est : ", statsPositive)
#print("Le nombre de poste negatives est : ", statsNegative)
#print("Le nombre de poste neutres est : ", statsNeutral)
#print("Le nombre de poste sans sentiment est : ", statsElse)

end = time.time()
print(end-start)