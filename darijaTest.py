# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 17:10:27 2019

@author: user
"""

url = "view-source:http://www.speakmoroccan.com/verbs-in-moroccan-arabic/?fbclid=IwAR2eMjQroQ_pb5BT9XultDq9UswtihgFkb4GVGcgRFiu1IYinlj8GB3fW1w"
browser.get(url)
liste = browser.find_elements_by_tag_name('td')

i = 1

slash = chr(47)
backslash = chr(92) 
file = open('DarijaDataset.txt','w',encoding="utf-8")
for l in liste1:
    file.write(l.text)
with open('DarijaDatasetfixed.txt','r',encoding="utf-8") as file1 :
    #filedata = file.readline()
    for line in file1:
        if i%3 == 0 :
            #line = line.replace("/ ", "/")
            #line = line.replace(" /", "/")
            #line = line.replace(" / ", "/")
            line = line.replace("\n",";")
        print(line)
        file.write(line)
        i = i + 1
        #print(i)
            
with open('DarijaDataset.txt','r',encoding="utf-8") as file :
    filedata = file.read()
    
filedata = filedata.replace("/","/")
filedata = filedata.replace("/ ","/")
filedata = filedata.replace(" /","/")
filedata = filedata.replace(" / ","/")
filedata = filedata.replace(","," ")
filedata = filedata.replace("…","") 
filedata = filedata.replace("...","") 
filedata = filedata.replace("\n",":") 
splitdata = filedata.split(";")
#print(filedata)
length = len(splitdata)
print(length)
print(splitdata)

    
for j in range(0,49):
        lineList = splitdata[j].split(":")
        #column0 = lineList[0]
        #1print(column0)
        #column1 = lineList[1]
        #print(column1)
        #column2 = lineList[2]
        #print(column2)
        #data = [column0,column1,column2]
        #splitList = FileData[j].split('|') 
            #m = re.search('(.+?).(.+?)',splitList[3] )
            #print(m)
            #print(splitList[0]) 
            #print(splitList[1]) 
            #print(splitList[2]) 
            #print(splitList[3]) 
            #print(splitList[4])   
            #var1 = splitList[1].split('.').join([[0]splitList[1].split('.')[1]])
            #print(var1)
        #csv.write(str(j) + "," + column0 + "," + column1 + "," + column2 + "\n")