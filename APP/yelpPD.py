from __future__ import division
import json #or cjson
import re
from stemming.porter2 import stem
from operator import itemgetter
from math import log
from collections import defaultdict
import operator
from Tkinter import *
from PIL import Image, ImageTk
from Tkinter import Tk, RIGHT, BOTH, RAISED
from ttk import Frame, Button, Style
import json #or cjson
import re

business_list = []
master = ''
submitted_text = ''
star_score = 0



class Hw1(object):
    
    def __init__(self):
        pass
    @staticmethod
    def read_line(a_json_string_from_document):
        #sample answer:
        return json.loads(a_json_string_from_document)
    @staticmethod
    def tokenize(string):
        unicode_word=re.findall(r'\w+',string.lower())
        return [str(word) for word in unicode_word ]
    #return a list of words
    
    @staticmethod
    def stopword(a_list_of_words):
        stopword = []
        for line in open('stop_word','r'):
            stopword.append(re.split('\n',line)[0])
        new_list=[word for word in a_list_of_words if word not in stopword]
        return new_list
    #or alternatively use new_list=filter(lambda x: x not in stopword, a_list_of_words)
    #return a list of words
    @staticmethod
    def stemming(a_list_of_words):
        stems=[stem(word) for word in a_list_of_words]
        return stems
#return a list of words

list5 = []
list4 = []
list3 = []
list2 = []
list1 = []


def openfiles():
	star5 = open('star5.json', 'r')
	star4 = open('star4.json', 'r')
	star3 = open('star3.json', 'r')
	star2 = open('star2.json', 'r')
	star1 = open('star1.json', 'r')
	for line in star5:
		list5.append(line)
	for line in star4:
		list4.append(line)
	for line in star3:
		list3.append(line)
	for line in star2:
		list2.append(line)
	for line in star1:
		list1.append(line)
	
	


def cosine(tfidf,tf_query):
    cosine_similarity=defaultdict(dict)
    rank_dict={}
    for key in tfidf.keys():
        for key1 in tf_query.keys():
            if key== key1:
                cosine_similarity[key][key1]=-1
            else:
                similarity=0
                a=tfidf[key].keys()
                b=tf_query[key1].keys()
                intersect= [val for val in  a if val in b]
                for word in intersect:
                    similarity+=tfidf[key][word]*tf_query[key1][word]
                cosine_similarity[key][key1]=similarity
                #Getting the top 10 pairs
        rank_dict[key+' '+key1]=similarity
    top10=sorted(rank_dict.iteritems(), key=itemgetter(1),reverse=1)[0:10] #they shown up in pairs, so keep 20.
    sum_1 = 0
    for x in top10:
      sum_1 = sum_1+x[1]
    return sum_1/10
		
def tf_calc(list1,my_list):
    tf=defaultdict(dict)
    idf={}# idf dictionary of terms
    rid_mapper={}# map id number to the line number
    num_line=1
    #my_list = list(["hello hi there"])
    new_list_use = list()
    for word in my_list[0].split(" "):
      new_list_use.append(word)

    #list1 = list(["i live in hello", "my name is hi hi hi hello there there", "hi hello waddup", "flavor is not good"])
    '''
    list_new = list()
    for word in my_list:
      for line in list1:
        if word in line.split(" "):
          print word, " is there "
        else: 
          print word, " nope "
    '''
    for word in new_list_use:
      num_line = 0
      for line in list1:
        num_line += 1
        r_id = "doc" + str(num_line)
        if word not in tf[r_id].values():
            tf[r_id][word] = 0
            idf[word] = 0
    #for word in new_list_use:
    
    num_line = 0
    for word in idf.keys():
        for line in list1:
          if word in line.split(" "):
            idf[word] += 1

    for line in list1:
      num_line += 1
      r_id = "doc" + str(num_line)
      for word in line.split(" "):
        if word in tf[r_id]:
          tf[r_id][word] += 1
    for key,value in idf.iteritems():
      if value != 0:
        idf[key]=log(num_line/int(value)) #idf defination:number of document/ number of document has the key

    
    for key,value in tf.iteritems():
        sum_tfidf=0
        for word,tfreq in value.iteritems():
            tf[key][word]=tfreq*idf[word]
            sum_tfidf+=(tfreq*idf[word])**2
        sum_tfidf=sum_tfidf**0.5
        #normalize the tfidf vector to unit length
        for word,tfidf in value.iteritems():
          if sum_tfidf != 0:
            tf[key][word]=tf[key][word]/sum_tfidf
    return tf

def similarity_score(user_review):
    
    #user_review = input("Enter your review: ")
    line1 = Hw1.tokenize(user_review)
    line2 = []
    line3 = []
    #for word in line1:
    line2 = Hw1.stemming(line1)
    line3 = Hw1.stopword(line2)

    print "list_new: " , line3
    my_list1 = " ".join(line3)
    my_list = []
    my_list.append(my_list1)

    #my_list = list(["pre charter terribl talk sell worthless rude servic avoid repres unhelp main compani program accept outag robot plagu servic unreli midst goal"])
    tf1 = tf_calc(list1[0:2000],my_list) 
    tf2 = tf_calc(list2[0:2000],my_list)
    tf3 = tf_calc(list3[0:2000],my_list)
    tf4 = tf_calc(list4[0:2000],my_list)
    tf5 = tf_calc(list5[0:2000],my_list)
    tf_query=defaultdict(dict)
    idf_query={}# idf dictionary of terms
    rid_mapper_query={}# map id number to the line number
    num_line=1
    for line in my_list:
        num_line+=1
        r_id= "doc"+str(num_line)
        for word in line.split(" "):
            if word in tf_query[r_id].keys():
                tf_query[r_id][word]+=1
            else:
                tf_query[r_id][word]=1
                #if show up first time in a document, count idf++
                if word in idf_query.keys():
                    idf_query[word]+=1
                else:
                    idf_query[word]=1
    for key,value in idf_query.iteritems():
        idf_query[key]=log(2/value) #idf defination:number of document/ number of document has the key
    
    for key,value in tf_query.iteritems():
        sum_tfidf=0
        for word,tfreq in value.iteritems():
            tf_query[key][word]=tfreq*idf_query[word]
            sum_tfidf+=(tfreq*idf_query[word])**2
        sum_tfidf=sum_tfidf**0.5
        #normalize the tfidf vector to unit length
        for word,tfidf in value.iteritems():
          if sum_tfidf !=0:
            tf_query[key][word]=tf_query[key][word]/sum_tfidf
    dictionary = {}

    dictionary[1] = cosine(tf1,tf_query)
    dictionary[2] = cosine(tf2,tf_query)
    dictionary[3] = cosine(tf3,tf_query)
    dictionary[4] = cosine(tf4,tf_query)
    dictionary[5] = cosine(tf5,tf_query)
    final_dict = sorted(dictionary.items(), key = operator.itemgetter(1), reverse = True)
    print "Final Review: " ,final_dict[0][0]
    return final_dict[0][0]
    
def get_rating(input):
    score1 = similarity_score(input)
    score2 = score1
    score3 = score1  
    rating = (score1+score2+score3)/3.0 
    return round(rating,0)

class display1(Frame): 
    
    def __init__(self,parent):
        Frame.__init__(self,parent)   
         
        self.parent = parent
        
        self.initUI()
        
    def initUI(self):
        
        
        w = Label(self, text="This is YelpPD")
        w.pack()  
        listbox = Listbox(self, height=10)
        for i in business_list:
            listbox.insert(END, i['name'])
        scrollbar = Scrollbar(self,orient=VERTICAL)
        scrollbar.configure(command=listbox.yview)
        listbox.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=LEFT, fill=Y) 
        listbox.pack(side=LEFT, fill=Y)    
        
        scrollbar.config(command=listbox.yview)    
        reviewbutton = Button(self, text="Write a Review",command=self.toreview) 
        reviewbutton.pack(side=BOTTOM, fill=X)   
        self.pack(fill=BOTH, expand=1)
        
    def toreview(self):         
        self.pack_forget()           
        display2(master)
        
class display2(Frame): 
       
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        
        self.initUI()
        
    def initUI(self):
        w = Label(self, text="Write a Review")        
        w.pack()          
        review_text = StringVar()     
        e = Entry(self, textvariable=review_text)
        review_text.set("Insert Review Here")    
        e.pack(side=TOP, fill=BOTH)
        b = Button(self, text="Submit Review",command=lambda: self.tostars(e.get()))
        b.pack(side=BOTTOM, fill=BOTH)
        self.pack(fill=BOTH, expand=1)
    
    def tostars(self,text): 
        global submitted_text,star_score
        submitted_text = text
        star = get_rating(text)
        
        star_score = star 
        self.pack_forget()          
        display3(master)

class display3(Frame):
     
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        
        self.initUI()
        
    def initUI(self):
        w = Label(self, text="The Predicted Star Value")
        w.pack() 
        global star_score
        image = Image.open("stars_0.png")
        star = star_score
        if (star == 1):
            image = Image.open("stars_1.png")
        if (star == 2):
            image = Image.open("stars_2.png")
        if (star == 3):
            image = Image.open("stars_3.png")
        if (star == 4):
            image = Image.open("stars_4.png")
        if (star == 5):
            image = Image.open("stars_5.png")
        
       
        photo = ImageTk.PhotoImage(image) 
        label = Label(self,image=photo)
        label.image = photo 
        label.pack()          
        T = Text(self, height=5, width=80)
        T.pack()
        Textbox = submitted_text
        T.insert(END, Textbox)         
        b1 = Button(self, text="Write another review", command=self.toreview)
        b2 = Button(self, text="Change Restaurant", command=self.tolist)
        b1.pack()             
        b2.pack()
        self.pack(fill=BOTH, expand=1)
        
    def toreview(self): 
        self.pack_forget()   
        display2(master)
    
    def tolist(self): 
        self.pack_forget()   
        display1(master)  

def loadbusiness():
    infilename='yelp_academic_dataset_business.json'
    f=open(infilename,'r')
    for line in f:
        business_list.append(json.loads(line))
   
        
        
def main():
    global master
    master  = Tk()
    master.title("YelpPD")
    master.geometry("700x700")  
    loadbusiness() 
    openfiles() 
    display1(master)    
    mainloop()
    
if __name__ == '__main__':
    main()  
