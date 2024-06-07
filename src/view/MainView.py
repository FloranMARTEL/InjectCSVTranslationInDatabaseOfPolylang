from tkinter import *

from controleur.ControleurSelectFile import ControleurSelectFile
from controleur.ControleurUpdateDatabase import ControleurUpdateDatabase
from view.EntryInput import EntryInput


#,borderwidth=1, relief="solid"
class MainView(Tk):

    def __init__(self) -> None:
        super().__init__()

        mainFrame = Frame(self)

        self.title("Traduction")

        #top
        dataBaseBox = Frame(mainFrame)
        titleDataBase = Label(dataBaseBox,text="DataBase")

        self.entryinputUser = EntryInput(dataBaseBox,text="user",value="root")
        self.entryinputPassword = EntryInput(dataBaseBox,"password",value="")
        self.entryinputHost = EntryInput(dataBaseBox,text="host",value="127.0.0.1")
        self.entryinputPort = EntryInput(dataBaseBox,text="port",value="3306")
        self.entryinputDatabase = EntryInput(dataBaseBox,text="database",value="www_guillemot")

        padyinputlistDatabase = 2.5
        titleDataBase.grid(row=0,column=0,pady=padyinputlistDatabase)
        self.entryinputUser.grid(row=1,column=0,pady=padyinputlistDatabase,sticky =E)
        self.entryinputPassword.grid(row=2,column=0,pady=padyinputlistDatabase,sticky =E)
        self.entryinputHost.grid(row=3,column=0,pady=padyinputlistDatabase,sticky =E)
        self.entryinputPort.grid(row=4,column=0,pady=padyinputlistDatabase,sticky =E)
        self.entryinputDatabase.grid(row=5,column=0,pady=padyinputlistDatabase,sticky =E)

        dataBaseBox.grid(row=0,column=0,sticky= W+E,pady=5)

        #midel
        csvBox = Frame(mainFrame)

        titlecsv = Label(csvBox,text="CSV")

        inputcsvBox = Frame(csvBox)

        self.entryFile = EntryInput(inputcsvBox,"Path : ")
        self.buttonselectFile : Button = Button(inputcsvBox,text="choose file")

        self.entryFile.grid(row=0,column=0)
        self.buttonselectFile.grid(row=0,column=1)

        titlecsv.grid(row=0,column=0)
        inputcsvBox.grid(row=1,column=0)

        csvBox.grid(row=1,column=0,pady=10)

        #bottom
        self.buttonCsvtowpjson = Button(mainFrame, text="Update DataBase")

        self.buttonCsvtowpjson.grid(row=2,column=0,sticky='nesw',pady=5)

        mainFrame.pack(padx=10,pady=5)

        self.fixbutton()


    

    def fixbutton(self):
        controleur = ControleurSelectFile(self.entryFile)
        self.buttonselectFile.bind("<Button-1>",controleur.Onclique)

        controleurUpdate = ControleurUpdateDatabase(self.entryFile,self.entryinputUser,self.entryinputPassword,self.entryinputHost,self.entryinputPort,self.entryinputDatabase)
        self.buttonCsvtowpjson.bind("<Button-1>",controleurUpdate.Onclique)





    




