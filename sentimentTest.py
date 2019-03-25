# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 11:51:02 2019

@author: user
"""

"""
analysis = TextBlob(line3)
analysis = TextBlob(line2)
analysis = TextBlob(line3)
analysis = TextBlob(line4)
"""
"""
pos_count = 0
pos_correct = 0
for l in line:
    analysis = TextBlob(l)
    
    if analysis.sentiment.polarity >= 0.01:
        if analysis.sentiment.polarity > 0:
            pos_correct += 1
        pos_count +=1

neg_count = 0
neg_correct = 0

for l in line:
    analysis = TextBlob(l)
    if analysis.sentiment.polarity <= -0.01:
        if analysis.sentiment.polarity <= 0:
            neg_correct += 1
        neg_count +=1

print("Positive accuracy = {}% via {} samples".format(pos_correct/pos_count*100.0, pos_count))
print("Negative accuracy = {}% via {} samples".format(neg_correct/neg_count*100.0, neg_count))

"""