from Tkinter import *

window  = Tk()

window.title("YelpPD")
window.geometry("700x700")

'''
app = Frame(window)
app.grid()
label = Label(app, text = "YelpPd")
label.grid()
'''

windowmode = 'list'

def toreview():
        print "it came here"
        windowmode = 'write'

def callback():
        print "click!"

w = Label(window, text="This is YelpPD")
w.pack()
if(windowmode == 'list'):
    scrollbar = Scrollbar(window)
    scrollbar.pack(side=RIGHT, fill=Y)    
    listbox = Listbox(window, yscrollcommand=scrollbar.set)
    for i in range(10):
        listbox.insert(END, str(i))
    listbox.pack(side=LEFT, fill=BOTH)    
    scrollbar.config(command=listbox.yview)
    reviewbutton = Button(window, text="Write Review",command=toreview)
    reviewbutton.pack()
    

if(windowmode == 'write'):
    T = Text(window, height=5, width=80)
    T.pack()
    T.insert(END, "Insert Review here")    
    b = Button(window, text="Sumbit Review", command=callback)
    b.pack()
    
window.update()
window.mainloop()