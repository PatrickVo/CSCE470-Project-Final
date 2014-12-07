import json
import re
from math import *
from operator import itemgetter

def tokenize(string):
    unicode_word=re.findall(r'\w*[a-zA-Z0-9]',string.lower())
    return [str(word) for word in unicode_word ]

def stopword(a_list_of_words):
    stopword = []
    for line in open('stop_word','r'):
        stopword.append(re.split('\n',line)[0])
    new_list=[word for word in a_list_of_words if word not in stopword]
    return new_list


list5 = []
list4 = []
list3 = []
list2 = []
list1 = []

star5 = open('star5.json', 'r')
star4 = open('star4.json', 'r')
star3 = open('star3.json', 'r')
star2 = open('star2.json', 'r')
star1 = open('star1.json', 'r')

cnt = 0
for line in star5:
    if cnt < 5000:
	list5.append(tokenize(line))
    cnt += 1
    
cnt = 0
for line in star4:
    if cnt < 5000:
	list4.append(tokenize(line))
    cnt += 1
    
cnt = 0
for line in star3:
    if cnt < 5000:
	list3.append(tokenize(line))
    cnt += 1
    
cnt = 0
for line in star2:
    if cnt < 5000:
	list2.append(tokenize(line))
    cnt += 1
    
cnt = 0
for line in star1:
    if cnt < 5000:
	list1.append(tokenize(line))
    cnt += 1

def wordcount(list):
    count = 0
    for line in list:
        for i in line:
            count += 1
    return count

def lm(query):
    star1_score = 0
    star2_score = 0
    star3_score = 0
    star4_score = 0
    star5_score = 0
    query_list = stopword(tokenize(query))

    wordcount1 = wordcount(list1)
    wordcount2 = wordcount(list2)
    wordcount3 = wordcount(list3)
    wordcount4 = wordcount(list4)
    wordcount5 = wordcount(list5)
    

    for d in list5: #calculate score for star5 list
        for q in query_list:
            tf = 0
            token_in_doc_count = 0
            for i in d:
                token_in_doc_count += 1
                if (q == i):
                    tf += 1
            if token_in_doc_count == 0:
                token_in_doc_count = 1
            a = ( float(tf) / float(token_in_doc_count) )
            b = (float(tf) / float(wordcount5))
            star5_score += (0.7 * a + 0.3 * b)
    star5_score = log(star5_score)

    for d in list4: #calculate score for star4 list
        for q in query_list:
            tf = 0
            token_in_doc_count = 0
            for i in d:
                token_in_doc_count += 1
                if (q == i):
                    tf += 1
            if token_in_doc_count == 0:
                token_in_doc_count = 1
            a = ( float(tf) / float(token_in_doc_count) )
            b = (float(tf) / float(wordcount4))
            star4_score += (0.7 * a + 0.3 * b)
    star4_score = log(star4_score)

    for d in list3: #calculate score for star3 list
        for q in query_list:
            tf = 0
            token_in_doc_count = 0
            for i in d:
                token_in_doc_count += 1
                if (q == i):
                    tf += 1
            if token_in_doc_count == 0:
                token_in_doc_count = 1
            a = ( float(tf) / float(token_in_doc_count) )
            b = (float(tf) / float(wordcount3))
            star3_score += (0.7 * a + 0.3 * b)
    star3_score = log(star3_score)

    for d in list2: #calculate score for star2 list
        for q in query_list:
            tf = 0
            token_in_doc_count = 0
            for i in d:
                token_in_doc_count += 1
                if (q == i):
                    tf += 1
            if token_in_doc_count == 0:
                token_in_doc_count = 1
            a = ( float(tf) / float(token_in_doc_count) )
            b = (float(tf) / float(wordcount2))
            star2_score += (0.7 * a + 0.3 * b)
    star2_score = log(star2_score)

    for d in list1: #calculate score for star1 list
        for q in query_list:
            tf = 0
            token_in_doc_count = 0
            for i in d:
                token_in_doc_count += 1
                if (q == i):
                    tf += 1
            if token_in_doc_count == 0:
                token_in_doc_count = 1
            a = ( float(tf) / float(token_in_doc_count) )
            b = (float(tf) / float(wordcount1))
            star1_score += (0.7 * a + 0.3 * b)
    star1_score = log(star1_score)

    top_score = star1_score
    if star2_score > top_score:
        top_score = star2_score
    if star3_score > top_score:
        top_score = star3_score
    if star4_score > top_score:
        top_score = star4_score
    if star5_score > top_score:
        top_score = star5_score
        
    print star1_score
    print star2_score
    print star3_score
    print star4_score
    print star5_score

    if top_score == star1_score:
        return 1
    if top_score == star2_score:
        return 2
    if top_score == star3_score:
        return 3
    if top_score == star4_score:
        return 4
    if top_score == star5_score:
        return 5


print lm("Horrible service! Their delivery driver whose name is apparently Wendy according to their cashier showed up at my door and when I asked how she was doing she went off on a rant about how horrible people are and how everyone should tip since she is 'wasting' her gas for them....as if she doesn't get paid at this job....and straight up told me that I should be cooking my own dinner if I can't afford to tip.")
