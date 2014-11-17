import json #or cjson
from json import dumps, load
import re
from stemming.porter2 import stem
from collections import Counter

def tokenize(string):        
    return re.findall(r'\w*[a-zA-Z0-9]',str(string.lower().encode('utf8')))
        
def stopword(a_list_of_words):        
    stopfilename = 'stop_word'
    stop_file=open(stopfilename,'r')
    stop_word_list = re.findall(r'\w*[a-zA-Z0-9]',str(stop_file.read()))
    return list(set(a_list_of_words) - set(stop_word_list))        

def stemming(a_list_of_words):    
    size = 0
    length = len(a_list_of_words)
    while(size<length):
        a_list_of_words[size] = stem(a_list_of_words[size])
        size+=1            
    return a_list_of_words 


class Hw1(object):
    def __init__(self):
        pass

    @staticmethod
    def read_line(a_json_string_from_document):
        #sample answer:x`
        return json.loads(a_json_string_from_document)
        

infilename='review.json'
f=open(infilename,'r')
ratings = {'0': 0}
count = 0
line_num = 1

star1 = open('star1.json', 'w')
star2 = open('star2.json', 'w')
star3 = open('star3.json', 'w')
star4 = open('star4.json', 'w')
star5 = open('star5.json', 'w')

dict1 = []
dict2 = []
dict3 = []
dict4 = []
dict5 = []

#1125459
while (line_num < 1125459):
    line_num += 1
    item = Hw1.read_line(f.readline())
    rating = int(item['stars'])
    text = item['text']
    
    list_text = tokenize(text)
    list_text = stopword(list_text)
    list_text = stemming(list_text)
    final_text = ' '.join(list_text)
    
    if(rating == 5):
        dict5.append(final_text)
    if(rating == 4):
        dict4.append(final_text)
    if(rating == 3):
        dict3.append(final_text)
    if(rating == 2):
        dict2.append(final_text)
    if(rating == 1):
        dict1.append(final_text)

json.dump(dict5,star5, indent=4) 
json.dump(dict4,star4, indent=4)  
json.dump(dict3,star3, indent=4)  
json.dump(dict2,star2, indent=4) 
json.dump(dict1,star1, indent=4) 