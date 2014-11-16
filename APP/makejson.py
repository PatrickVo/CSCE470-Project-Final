import json #or cjson
from json import dumps, load

class Hw1(object):
    def __init__(self):
        pass

    @staticmethod
    def read_line(a_json_string_from_document):
        #sample answer:
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


#1125459
while (line_num < 1000):
    line_num += 1
    item = Hw1.read_line(f.readline())
    rating = int(item['stars'])
    text = item['text']     
  
    if(rating == 5):
        dumps({'text':text},star5,indent=4)   
        '''    
    if(rating == 4):
        rate4.append(text)
    if(rating == 3):
        rate3.append(text)
    if(rating == 2):
        rate2.append(text)
    if(rating == 1):
        rate1.append(text)
        '''

        
star5.close
star4.close
star3.close
star2.close
star1.close

