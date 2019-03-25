# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 17:03:28 2019

@author: user
"""
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from lxml import html
#import requests 
from lxml.cssselect import CSSSelector
import csv
import unicodecsv
import pymongo
from pymongo import MongoClient

client = MongoClient()
client = MongoClient('localhost', 27017)
client = MongoClient('mongodb://localhost:27017/')

db = client.facebook
collection = db.dataset



chrome_path = r"scrape\chromedriver.exe"
options = webdriver.ChromeOptions()
browser = webdriver.Chrome(executable_path=chrome_path, options=options)

url = "http://www.speakmoroccan.com/50-basic-words-and-phrases-in-moroccan-arabic/?fbclid=IwAR3jP2N1OwrHHvqqEDUWXsEaMGCQAvHNzdnTUpNDJ2UuRGpiQUSIs7GnZgo"
browser.get(url)


csvDDS = "DarijaDataset.csv" #what name you want to save your csv as
csv = open(csvDDS, "w",encoding="UTF-16") #create or open csv, "w" to write strings  
colNames = "Number , English , Transcribed Moroccan Arabic , Moroccan Darija in Arabic Letters\n" #column titles
csv.write(colNames)

#liste = browser.find_element_by_class_name('row-hover')
liste = browser.find_elements_by_tag_name('td')
file = open('DarijaDataset.txt','w',encoding="utf-16")
i = 1
#elementArray = []

for elem in liste :
    #print(elem.text)
    data = elem.text
    #elementArray = elementArray.append(elem.text)
    if data == "Check out this list of 100 adjectives in Moroccan Arabic." :
        exit
    elif data == "Check out the lesson on the feminine form in Moroccan Arabic." :
        exit
    else:
        file.write(data + "\n")

#file = open('DarijaDataset.txt','w',encoding="utf-8")
#file.write(data)

slash = chr(47)
backslash = chr(92) 
file = open('DarijaDataset.txt','w',encoding="utf-16")

with open('DarijaDatasetfixed.txt','r',encoding="utf-8") as file1 :
    #filedata = file.readline()
    for line in file1:
        if i%3 == 0 :
            line = line.replace("\n","|")
        #print(line)
        file.write(line)
        i = i + 1
        #print(i)
            
with open('DarijaDataset.txt','r',encoding="utf-16") as file :
    filedata = file.read()
    
filedata = filedata.replace("/","/")
filedata = filedata.replace("/ ","/")
filedata = filedata.replace(" /","/")
filedata = filedata.replace(" / ","/")
filedata = filedata.replace(","," ")
filedata = filedata.replace("…","") 
filedata = filedata.replace("...","") 
filedata = filedata.replace("\n",":") 
splitdata = filedata.split("|")
#print(filedata)
length = len(splitdata)
print(length)
print(splitdata)

    
for j in range(0,49):
        lineList = splitdata[j].split(":")
        column0 = lineList[0]
        print(column0)
        column1 = lineList[1]
        print(column1)
        column2 = lineList[2]
        print(column2)
        data = [str(j),column0,column1,column2]
    
        data = [column0,column1,column2]
        word = {"Id": str(j),
                "English": column0,
                "Transcribed Moroccan Arabic": column1,
                "Moroccan Darija in Arabic Letters": column2}

        dataset = db.dataset
        word_id = dataset.insert_one(word).inserted_id
        print(word_id)
    
        #csv.write(str(j) + "," + column0 + "," + column1 + "," + column2 + "\n")
        csv.write(str(j) + "," + column0 + "," + column1 + "," + column2 + "\n")
        """
        with open('DarijaDataset.csv','wb') as f:
            w = unicodecsv.writer(f,encoding='utf-8')
            w.writerows(data)
        """
csv.close() 

