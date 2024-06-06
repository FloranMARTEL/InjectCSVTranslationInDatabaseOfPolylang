from tkinter import *

class Popup:
   
   def __init__(self,text) -> None:
        top= Toplevel()
        top.title("Popup")
        Label(top, text= text).pack(padx=10,pady=10)