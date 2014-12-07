from __future__ import division
from __future__ import with_statement
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


import math
import sys

import category_predictor

business_list =  []
master = ''
submitted_text = ''
business_index = 0
star_score = 0
read_size = 1500

def tokenize(string):
    unicode_word=re.findall(r'\w*[a-zA-Z0-9]',string.lower())
    return [str(word) for word in unicode_word ]

def stopword(a_list_of_words):
    stopword = []
    for line in open('stop_word','r'):
        stopword.append(re.split('\n',line)[0])
    new_list=[word for word in a_list_of_words if word not in stopword]
    return new_list


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

tlist5 = []
tlist4 = []
tlist3 = []
tlist2 = []
tlist1 = []


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
		
def openfilesLM():
    star5 = open('star5.json', 'r')
    star4 = open('star4.json', 'r')
    star3 = open('star3.json', 'r')
    star2 = open('star2.json', 'r')
    star1 = open('star1.json', 'r')
    cnt = 0
    for line in star5:
        if cnt < read_size:
   	    tlist5.append(tokenize(line))
        cnt += 1
        
    cnt = 0
    for line in star4:
        if cnt < read_size:
   	    tlist4.append(tokenize(line))
        cnt += 1
        
    cnt = 0
    for line in star3:
        if cnt < read_size:
   	    tlist3.append(tokenize(line))
        cnt += 1
        
    cnt = 0
    for line in star2:
        if cnt < read_size:
   	    tlist2.append(tokenize(line))
        cnt += 1
        
    cnt = 0
    for line in star1:
        if cnt < read_size:
   	    tlist1.append(tokenize(line))
        cnt += 1
        


class ReviewCategoryClassifier(object):

	@classmethod
	def load_data(cls, input_file):

		job = category_predictor.CategoryPredictor()

		category_counts = None
		word_counts = {}

		with open(input_file) as src:
			for line in src:
				category, counts = job.parse_output_line(line)

				if category == 'all':
					category_counts = counts
				else:
					word_counts[category] = counts

		return category_counts, word_counts

	@classmethod
	def normalize_counts(cls, counts):

		total = sum(counts.itervalues())
		lg_total = math.log(total)

		return dict((key, math.log(cnt) - lg_total) for key, cnt in counts.iteritems())

	def __init__(self, input_file):

		category_counts, word_counts = self.load_data(input_file)

		self.word_given_cat_prob = {}
		for cat, counts in word_counts.iteritems():
			self.word_given_cat_prob[cat] = self.normalize_counts(counts)

		# filter out categories which have no words
		seen_categories = set(word_counts)
		seen_category_counts = dict((cat, count) for cat, count in category_counts.iteritems() \
										if cat in seen_categories)
		self.category_prob = self.normalize_counts(seen_category_counts)

	def classify(self, text):

		lg_scores = self.category_prob.copy()

		for word in category_predictor.words(text):
			for cat in lg_scores:
				cat_probs = self.word_given_cat_prob[cat]

				if word in cat_probs:
					lg_scores[cat] += cat_probs[word]
				else:
					lg_scores[cat] += cat_probs['UNK']


		scores = dict((cat, math.exp(score)) for cat, score in lg_scores.iteritems())
		total = sum(scores.itervalues())
		return dict((cat, prob / total) for cat, prob in scores.iteritems())
        
def predictor(query):
    guesses = ReviewCategoryClassifier("review_new.json").classify(query)
    best_guesses = sorted(guesses.iteritems(), key=lambda (_, prob): prob, reverse=True)[:5]
    return best_guesses[0]
        

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
    

    for d in tlist5: #calculate score for star5 list
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

    for d in tlist4: #calculate score for star4 list
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

    for d in tlist3: #calculate score for star3 list
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

    for d in tlist2: #calculate score for star2 list
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

    for d in tlist1: #calculate score for star1 list
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

  
    my_list1 = " ".join(line3)
    my_list = []
    my_list.append(my_list1)

    #my_list = list(["pre charter terribl talk sell worthless rude servic avoid repres unhelp main compani program accept outag robot plagu servic unreli midst goal"])
    tf1 = tf_calc(list1[0:read_size],my_list) 
    tf2 = tf_calc(list2[0:read_size],my_list)
    tf3 = tf_calc(list3[0:read_size],my_list)
    tf4 = tf_calc(list4[0:read_size],my_list)
    tf5 = tf_calc(list5[0:read_size],my_list)
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
    return final_dict[0][0]
    
def get_rating(text):
    score1 = similarity_score(text)
    score2 = lm(text)    
    score3 = predictor(text)
    rating = (score1+score2+score3)/3.0 
    print score1
    print score2
    print score3
    return round(rating,0)

class display1(Frame): 
    
    def __init__(self,parent):
        Frame.__init__(self,parent)   
         
        self.parent = parent
        
        self.initUI()
        
    def initUI(self):

        w = Label(self, text="This is YelpPD")
        w.pack()  
        listbox = Listbox(self, height=20, width = 110)
        last_word = '' 
        for i in business_list:
            if last_word != i['name']:
                listbox.insert(END, i['name'])
                last_word = i['name']
        scrollbar = Scrollbar(self,orient=VERTICAL)
        scrollbar.configure(command=listbox.yview)
        listbox.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=LEFT, fill=Y) 
        listbox.pack()    
        
        scrollbar.config(command=listbox.yview)    
        reviewbutton = Button(self, text="Write a Review",command=lambda: self.toreview(listbox.curselection()[0])) 
        reviewbutton.pack(side=BOTTOM, fill=X)   
        self.pack(fill=BOTH, expand=1)
        
    def toreview(self,text):  
        global  business_index
        business_index = text 
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

        information = Label(self,text = business_list[int(business_index)]['stars'] )
        information.pack()     
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
        self.pack_forget()
        
        star_score = star 
                
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
    global business_list

    infilename='yelp_academic_dataset_business.json'
    f=open(infilename,'r')
    for line in f:
        load = json.loads(line)
        business_list.append(load)
    business_list = sorted(business_list,key=lambda x:x['name'])
   
        
        
def main():
    global master
    master  = Tk()
    master.title("YelpPD")
    master.geometry("900x900")  
    loadbusiness() 
    openfiles()
    openfilesLM() 
    display1(master)    
    mainloop()
    
if __name__ == '__main__':
    main()  
