from Tkinter import *
from PIL import Image, ImageTk
from Tkinter import Tk, RIGHT, BOTH, RAISED
from ttk import Frame, Button, Style
import json #or cjson
import re

business_list = []
master = ''
submitted_text = ''
      
class display1(Frame): 
    
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
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
        self.pack()
        
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
        self.pack()
    
    def tostars(self,text): 
        global submitted_text
        submitted_text = text
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
        image = Image.open("stars_3.png")
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
        self.pack()
        
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
    master  = Tk()
    master.title("YelpPD")
    master.geometry("700x700")  
    loadbusiness()  
    display1(master)    
    mainloop()
    
if __name__ == '__main__':
    main()  