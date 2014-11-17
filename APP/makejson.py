import json #or cjson
from json import dumps, load
import simplejson

def put(data, filename):
	jsondata = simplejson.dumps(data, indent=4, skipkeys=True, sort_keys=True)
	fd = open(filename, 'w')
	fd.write(jsondata)
	fd.close()

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

dict1 = dict()
dict2 = dict()
dict3 = dict()
dict4 = dict()
dict5 = dict()

#1125459
while (line_num < 1000):
    line_num += 1
    item = Hw1.read_line(f.readline())
    rating = int(item['stars'])
    text = item['text']     
  
    if(rating == 5):
        dict5[line_num] = text           
    if(rating == 4):
        dict4[line_num] = text
    if(rating == 3):
        dict3[line_num] = text
    if(rating == 2):
        dict2[line_num] = text
    if(rating == 1):
        dict1[line_num] = text
       

json.dump(dict5,star5, indent=0) 
json.dump(dict5,star5, indent=0)  
json.dump(dict5,star5, indent=0)  
json.dump(dict5,star5, indent=0) 
json.dump(dict5,star5, indent=0) 