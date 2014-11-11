from Tkinter import *
from PIL import Image, ImageTk

window  = Tk()

window.title("YelpPD")
window.geometry("700x700")

'''
app = Frame(window)
app.grid()
label = Label(app, text = "YelpPd")
label.grid()
'''

#windowmode = 'write'
windowmode = 'list'
#windowmode = 'finish'

def toreview():
        windowmode = 'write'      

def callback():
        print "click!"


if(windowmode == 'list'):
        w = Label(window, text="This is YelpPD")
        w.pack()  
        scrollbar = Scrollbar(window)
        scrollbar.pack(side=RIGHT, fill=Y)    
        listbox = Listbox(window, yscrollcommand=scrollbar.set)
        for i in range(10):
            listbox.insert(END, "Restaurant #"+str(i))
        listbox.pack(side=LEFT, fill=BOTH)    
        scrollbar.config(command=listbox.yview)    
        reviewbutton = Button(window, text="Write a Review",command=toreview) 
        reviewbutton.pack()    

if(windowmode == 'write'):
        w = Label(window, text="Write a Review")
        w.pack()          
        T = Text(window, height=5, width=80)
        T.pack()
        Textbox = "Insert Review here"
        T.insert(END, Textbox) 
        b = Button(window, text="Submit Review", command=callback)
        b.pack()     

if(windowmode == 'finish'):
        w = Label(window, text="The Predicted Star Value")
        w.pack() 
        image = Image.open("stars_3.png")
        photo = ImageTk.PhotoImage(image) 
        label = Label(image=photo)
        label.image = photo 
        label.pack()          
        T = Text(window, height=5, width=80)
        T.pack()
        Textbox = "Sumbited Review"
        T.insert(END, Textbox)         
        b1 = Button(window, text="Write another review", command=callback)
        b2 = Button(window, text="Chanage Restaurant", command=callback)
        b1.pack()             
        b2.pack()

window.mainloop()