from tkinter import *

class EntryInput(Frame):

    def __init__(self,master,text,value = ""):
        super().__init__(master)

        textinput = Label(self,text=text)

        self.entryInput = Entry(self)
        self.entryInput.insert(0,value)

        textinput.grid(row=0,column=0,sticky=W)
        self.entryInput.grid(row=0,column=1)