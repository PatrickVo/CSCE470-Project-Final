import json #or cjson
import re
from stemming.porter2 import stem
from operator import itemgetter
class Hw1(object):
    def __init__(self):
        pass
    @staticmethod
    def read_line(a_json_string_from_document):
        #sample answer:
        return json.loads(a_json_string_from_document)
    @staticmethod
    def tokenize(string):
        unicode_word=re.findall(r'\w+',string['text'].lower())
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
    
    def unigram_count(self, a_document_name):
        #TO NOTE, for this function, it's an default instance method,
        #in contrast to static method. When calling the function, you need to declare a class instance first.
        freqdict={}
        for line in open(a_document_name,'r'):
            line1=Hw1.read_line(line)
            line2=Hw1.tokenize(line1)
            line3=Hw1.stopword(line2)
            line4=Hw1.stemming(line3)
            for word in line4:
                if word in freqdict.keys():
                    freqdict[word]+=1
                else:
                    freqdict[word]=1
        return sorted(freqdict.iteritems(),key=itemgetter(1),reverse=1)[:20]
    
    #return top 20 unigrams e.g. {[hot,99],[dog,66],...}
    
    def bigram_count(self,a_document_name):
        freqdict={}
        for line in open(a_document_name,'r'):
            line1=Hw1.read_line(line)
            line2=Hw1.tokenize(line1)
            line3=Hw1.stopword(line2)
            #line4=Hw1.stemming(line3)
            
            for i in range(0,len(line3)-1):
                bigram=line3[i]+' '+line3[i+1]
                if bigram in freqdict.keys():
                    freqdict[bigram]+=1
                else:
                    freqdict[bigram]=1
        print sorted(freqdict.iteritems(),key=itemgetter(1),reverse=1)[:20]
#To note you may also use some one-line trick method like "counter()" function and here is a link http://stackoverflow.com/questions/12488722/counting-bigrams-pair-of-two-words-in-a-file-using-python
if __name__ == '__main__':
    #run this script to get top twenty bigrams
    hw=Hw1()
    hw.bigram_count('./review_KcSJUq1kwO8awZRMS6Q49g')