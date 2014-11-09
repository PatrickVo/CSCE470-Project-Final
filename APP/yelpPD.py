from Tkinter import *

window  = Tk()

window.title("YelpPD")
window.geometry("700x700")

app = Frame(window)
app.grid()
label = Label(app, text = "YelpPd")
label.grid()

window.mainloop()