# -*- coding: utf-8 -*-

from langdetect import detect
from langdetect import DetectorFactory 
import string 
import nltk
from nltk.corpus import stopwords
from textblob import TextBlob 
import langdetect 
import langid
from textblob.exceptions import TranslatorError, NotTranslated
from nltk.corpus import words
import  pymongo
from pymongo import MongoClient
import pprint
import time 

start = time.time()
client = MongoClient("mongodb://localhost:27017/facebook")
db = client.facebook
fb = db.fb

postsArray = []

for record in fb.find().limit(10):
     value = record["message"]
     postsArray.append(value)
     pprint.pprint(value)
     
print(postsArray)
#client.database_names()

#nltk.download('stopwords')
#x="This is an interesting sujet"
#x="Une bibliothèque ,Logicielle en words"
#x="Natural Language Toolkit السائحون رأوا غروب الشمس"
#x="new ad puts spotlight on women ... and it's glorious."
#x = "My sister got me un cadeau"
#x = "muchas gracias"

DetectorFactory.seed = 0
#is_uppercase_letter = True in map(lambda l: l.isupper(), x)
#print(is_uppercase_letter)
slash = chr(47)
backslash = chr(92)
char_list = ["!" , '"' , "#" , "$" , "%" , "&" , "'" , "(" , ")" , "+" , "*" , "-" , backslash , slash , "." , "," , 
             ":" , ";" , "<" , ">" , "=" , "?" , "@" , "[" , "]" , "^" , "_" , "`" , "{" , "}" , "|" , "~" , "²" , "£" , 
             "§"]
#wording = TextBlob("python")
#print(wording.detect_language())

def translateException(word,language):
    l = word.detect_language() 
    
    if NotTranslated :
        raise ValueError("The word is unchangeable")
        raise TypeError(translated = word.translate(to=language))
       
    #word = TextBlob(word)
    #word.translate(to=language)
    return word 

def wordExists(word,fileFR):
    
    file = open(fileFR,'r')
    #count = 0
    with open(fileFR,'r') as file :
            filedata = file.read()
    
    content = filedata.split("\t") 
    #print(content)
    #print(content.count(word))
    if content.count(word) != 0 :
        #print("it exists")
        return True 
    else :
        #print("it doesn't exist")
        return False 
        
language = 0 

word_list = words.words()

statsEN=0
statsFR=0
statsAR=0
statsUNKNOWN=0
statsEMPTY=0
fileFrench ='Lexique382.txt'
#analysis = str(analysis)
for x in postsArray :
    if not x :
        print("the post is empty")
        statsEMPTY+=1
        
    else:
        x=x.replace("ad","advertisement")
        #print(x)
        x = x.lower()
    
        for j in char_list:
            x = x.replace(j,"")
        newSentence = ''
        tokens = nltk.word_tokenize(x)
        tagged = nltk.pos_tag(tokens)
        length = len(tokens[0])
        testWord = x[0:length]
        #print(testWord)
        
        if length < 3:
            listOfStopWordsEN = stopwords.words('english')
            listOfStopWordsFR = stopwords.words('french')
            listOfStopWordsAR = stopwords.words('arabic')
            if listOfStopWordsEN.count(tokens[0]) == 1:
                detector = 'en'
            elif listOfStopWordsFR.count(tokens[0]) == 1:
                detector = 'fr'
            elif listOfStopWordsAR.count(tokens[0]) == 1:
                detector = 'ar'
        elif length >= 3:
            length = len(tokens[0])
            testWord = x[:length]
            #print(testWord)
            if word_list.count(testWord) == 1:
                detector = "en"
                
            elif  wordExists(testWord,fileFrench) == True:
                detector = "fr"
            #analysis = TextBlob(testWord)
            #detector = analysis.detect_language()
    
        if detector == 'fr':
            for word in tokens:
                #print(word)
                word= str(word)
                if len(word) >= 3:
                    analysis = TextBlob(word)      
                    if analysis.detect_language() == 'fr'  :
                        #newSentence = ' '.join(newSentence) 
                        newSentence = newSentence + " " + str(word) 

                    elif analysis.detect_language() == 'en':
                        #print("testing")
                        
                        #& word_list.count("python")
                        if wordExists(analysis,fileFrench) == True :
                            newSentence = newSentence + " " + str(word) 
                        elif wordExists(analysis,fileFrench) == False :
                            wordTranslated = analysis.translate(to='fr')
                            newSentence = newSentence + " " + str(wordTranslated) 
                    elif analysis.detect_language() == 'ar':
                            wordTranslated = analysis.translate(to='fr')
                            newSentence = newSentence + " " + str(wordTranslated) 
                    
                elif len(word) < 3:
                    listOfStopWordsFR = stopwords.words('french')
                    if listOfStopWordsFR.count(word) == 1:
                        #newSentence = ' '.join(newSentence) 
                        newSentence = newSentence + " " + str(word)
                        #print("3")
                    elif listOfStopWordsFR.count(word) == 0: 
                        #curentLang = analysis.detect_language()
                        wordTranslated = analysis.translate(to='fr')
                        #newSentence = ' '.join(wordTranslated)
                        newSentence = newSentence + " " + str(wordTranslated)
                        #print("4")
            #print('fr')
            print('The sentence: "' + newSentence + ' " is in fr' )
            statsFR+=1
            


        elif detector == 'en':
            #analysis = str(analysis)
            for word in tokens:
                #print(word)
                analysis = TextBlob(word)
                if len(analysis) >= 3:                  
                    if analysis.detect_language() == 'en':
                        #newSentence = ' '.join(newSentence)
                        #newSentence = newSentence.join(word)
                        newSentence = newSentence + " " + str(word) 
                        #print(newSentence)
                        #print("1")
                    elif analysis.detect_language() == 'fr':
                        #print("testing")
                        count = word_list.count(analysis)
                        #& word_list.count("python")
                        if count  != 0 :
                            newSentence = newSentence + " " + str(word) 
                            #print("2")
                        elif count == 0 :
                            wordTranslated = analysis.translate(to='en')
                            newSentence = newSentence + " " + str(wordTranslated) 
                            #print("3")
                    elif analysis.detect_language() == 'ar':
                            wordTranslated = analysis.translate(to='en')
                            newSentence = newSentence + " " + str(wordTranslated) 
                            #print("4")
                elif len(analysis) <= 3:
                    listOfStopWordsEN = stopwords.words('english')
                    if listOfStopWordsEN.count(analysis) == 1:
                        #newSentence = newSentence.join(word) 
                        newSentence = newSentence + " " + str(word) 
                        #print(newSentence)
                        #print("5")
                    elif listOfStopWordsEN.count(analysis) == 0:
                        wordTranslated = analysis.translate(to='en') 
                        #newSentence = newSentence.join(wordTranslated)
                        newSentence = newSentence + " " + str(wordTranslated)
                        #print("6")
            #print('en')
            print('The sentence: "' + newSentence + ' " is in en' )
            statsEN+=1
            
            #print(detect(newSentence))
        
        elif detector == 'ar':
            for word in tokens:
                #print(word)
                analysis = TextBlob(word)
                if len(word) >= 3:
                    #print(len(word))
                    if detect(str(analysis)) == 'ar':
                        #newSentence = ' '.join(newSentence) 
                        newSentence = newSentence + " " + str(word) 
                        #print("1")
                    elif detect(str(analysis)) != 'ar':
                        wordTranslated = analysis.translate(to='ar') 
                        #newSentence = ' '.join(wordTranslated)
                        newSentence = newSentence + " " + str(wordTranslated)
                elif len(analysis) < 3:
                    listOfStopWordsFR = stopwords.words('arabic')
                    if listOfStopWordsAR.count(word) == 1:
                        #newSentence = ' '.join(newSentence) 
                        newSentence = newSentence + " " + str(word)
                    elif listOfStopWordsEN.count(word) != 1:
                        wordTranslated = analysis.translate(to='ar') 
                        #newSentence = ' '.join(wordTranslated)
                        newSentence = newSentence + " " + str(wordTranslated)
            #print('ar')  
            print('The sentence: "' + newSentence + ' " is in ar' )
            statsAR+=1
            
        elif not filter(lambda x: x in detector, ["en","ar","fr"]): 
            print("Unknown language")
            statsUNKNOWN+=1
            
           
print("Le nombre de poste vides est: " ,statsEMPTY)
print("Le nombre de poste ecrits en Francais est: " ,statsFR)        
print("Le nombre de poste ecrits en Anglais est: " ,statsEN)
print("Le nombre de poste ecrits en Arabe est: " ,statsAR)       
print("Le nombre de poste ecrits en une langue inconnue est: " ,statsUNKNOWN)

end = time.time()
print(end-start)
print((((end-start)*1000000)/60)/60)





