# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 15:29:10 2019

@author: user
"""

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

#client.database_names()

#nltk.download('stopwords')
#x="This is an interesting sujet"
#x="Une bibliothèque ,Logicielle en words"
#x="Natural Language Toolkit السائحون رأوا غروب الشمس"
#x="new ad puts spotlight on women ... and it's glorious."
#x = "My sister got me un cadeau"
#x = "muchas gracias"
#wording = TextBlob("python")
#print(wording.detect_language())

def cleanSentence(sentence):
    DetectorFactory.seed = 0
    #is_uppercase_letter = True in map(lambda l: l.isupper(), sentence)
    #print(is_uppercase_letter)
    slash = chr(47)
    backslash = chr(92)
    char_list = ["!" , '"' , "#" , "$" , "%" , "&" , "'" , "(" , ")" , "+" , "*" , "-" , backslash , slash , "." , "," , 
             ":" , ";" , "<" , ">" , "=" , "?" , "@" , "[" , "]" , "^" , "_" , "`" , "{" , "}" , "|" , "~" , "²" , "£" , 
             "§"]
    for j in char_list:
        sentence = sentence.replace(j,"")
    
    sentence = sentence.replace("ad","advertisement")
    #print(x)
    sentence = sentence.lower()
    return sentence 

#print(cleanSentence("Une bibliothèque ,Logicielle en words"))
    
def translateException(word,language):
    l = word.detect_language() 
    
    if NotTranslated :
        raise ValueError("The word is unchangeable")
        raise TypeError(translated = word.translate(to=language))
    return word 

def wordExists(word,path=""):
    
    #file = open(fileFR,'r')
    with open(path,'r') as file :
            filedata = file.read()
    
    content = filedata.split("\t") 
    if content.count(word) != 0 :
        return True 
    else :
        return False 

def tokenizingSentence(sentence):
    newS = cleanSentence(sentence)
    tokens = nltk.word_tokenize(newS)
    #tagged = nltk.pos_tag(tokens)
    return tokens 

#print(testWord)
def defineSentenceLang(sentence):
    tokens = tokenizingSentence(sentence)
    length = len(tokens[0])
    testWord = sentence[0:length]
    
    word_list = words.words()
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
        testWord = sentence[0:length]
        #print(testWord)
        #analysis = TextBlob(testWord)
        #detector = analysis.detect_language()
        #print(testWord)
        if word_list.count(testWord) == 1:
                #print("its english")
                detector = "en"     
        elif  wordExists(testWord,'Lexique382.txt') == True:
                #print("its french")
                detector = "fr"
        
    return detector 

    #print(analysis.detect_language())
#print(defineSentenceLang("Une bibliothèque ,Logicielle en words"))
#print("end of test")
#print("why the f wouldn't work")

#print(length)
#splittext = x.split(" ")
#print(splittext[0])
#print(detect(splittext[0]))
#print(tokens[0])
    
def detectPlusTranslate(sentence):
    word_list = words.words()
    newSentence = ''
    if not sentence:
        #print("post is empty can't detect lang")
        return "the post is empty"
    else:
        #analysis = str(analysis)
        detector = defineSentenceLang(sentence)
        if detector == 'fr':
            tokens = tokenizingSentence(sentence)
            for word in tokens:
                #print(word)
                word= str(word)
                if len(word) >= 3:
                    analysis = TextBlob(word)      
                    if analysis.detect_language() == 'fr'  :
                        newSentence = newSentence + " " + str(analysis) 
                    elif analysis.detect_language() == 'en':
                        pathfile = "Lexique382.txt"
                        if wordExists(analysis,pathfile) == True :
                            newSentence = newSentence + " " + str(analysis) 
                        elif wordExists(analysis,pathfile) == False :
                            wordTranslated = analysis.translate(to='fr')
                            newSentence = newSentence + " " + str(wordTranslated) 
                    elif analysis.detect_language() == 'ar':
                            wordTranslated = analysis.translate(to='fr')
                            newSentence = newSentence + " " + str(wordTranslated) 
                    else:
                        newSentence = newSentence + " " + str(analysis) 
                        
                elif len(analysis) < 3:
                    
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
            #print(newSentence.detect_language())
            #print('fr')
            #print(newSentence)
            #return 'The sentence ' + newSentence + ' is in fr'
            return "French"
    
    
        elif detector == 'en':
            #analysis = str(analysis)
            tokens = tokenizingSentence(sentence)
            for word in tokens:
                #print(word)
                analysis = TextBlob(word)
                if len(analysis) >= 3:                  
                    if analysis.detect_language() == 'en':
                        newSentence = newSentence + " " + str(analysis) 
                        #print(newSentence)
                    elif analysis.detect_language() == 'fr':
                        count = word_list.count(analysis)
                        if count  != 0 :
                            newSentence = newSentence + " " + str(analysis) 
                            #print(newSentence)
                            #print("2")
                        elif count == 0 :
                            wordTranslated = analysis.translate(to='en')
                            newSentence = newSentence + " " + str(wordTranslated) 
                            #print(newSentence)
                            #print("3")
                    elif analysis.detect_language() == 'ar':
                            wordTranslated = analysis.translate(to='en')
                            newSentence = newSentence + " " + str(wordTranslated) 
                            #print(newSentence)
                    else:
                        newSentence = newSentence + " " + str(analysis) 
                        
                            #print("4")
                elif len(analysis) < 3:
                    listOfStopWordsEN = stopwords.words('english')
                    if listOfStopWordsEN.count(analysis) == 1:
                        #newSentence = newSentence.join(word) 
                        newSentence = newSentence + " " + str(analysis) 
                        #print(newSentence)
                        #print("5")
                    elif listOfStopWordsEN.count(analysis) == 0:
                        wordTranslated = analysis.translate(to='en') 
                        #newSentence = newSentence.join(wordTranslated)
                        newSentence = newSentence + " " + str(wordTranslated)
                        #print(newSentence)
                        
                        #print("6")
                        
                #print(analysis)
            #print('en')
            #print(newSentence)
            #return 'The sentence ' + newSentence + ' is in en' 
            #print(detect(newSentence))
            return "English"
        elif detector == 'ar':
            tokens = tokenizingSentence(sentence)
            for word in tokens:
                #print(word)
                analysis = TextBlob(word)
                if len(word) >= 3:
                    #print(len(word))
                    if detect(str(analysis)) == 'ar':
                        #newSentence = ' '.join(newSentence) 
                        newSentence = newSentence + " " + str(analysis) 
                        #print("1")
                    elif detect(str(analysis)) != 'ar':
                        wordTranslated = analysis.translate(to='ar') 
                        #newSentence = ' '.join(wordTranslated)
                        newSentence = newSentence + " " + str(wordTranslated)
                    else:
                        newSentence = newSentence + " " + str(analysis) 
                        
                elif len(analysis) < 3:
                    listOfStopWordsAR = stopwords.words('arabic')
                    if listOfStopWordsAR.count(word) == 1:
                        #newSentence = ' '.join(newSentence) 
                        newSentence = newSentence + " " + str(analysis)
                    elif listOfStopWordsAR.count(word) != 1:
                        wordTranslated = analysis.translate(to='ar') 
                        #newSentence = ' '.join(wordTranslated)
                        newSentence = newSentence + " " + str(wordTranslated)
            #print('ar')  
            #print(newSentence)
            #return 'The sentence ' + newSentence + ' is in ar' 
            return "Arabic"
            
        elif detector not in ["ar","fr","en"]:
            #print("Unknown language")
            return "Unknown language" 

#print(detectPlusTranslate("dove provides the best care"))


