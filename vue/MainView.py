from tkinter import *


class MainView(Tk):

    def __init__(self) -> None:
        super().__init__()

        mainFrame = Frame(self)




        #top
        fileBox = Frame(mainFrame)
        urlEntry = Entry(fileBox)
        buttonFindFile = Button(fileBox, text="file")

        urlEntry.grid(row=0,column=0)
        buttonFindFile.grid(row=0,column=1)

        fileBox.grid(row=0,column=0)

        #midel
        buttonCsvtowpjson = Button(mainFrame, text="↓")

        buttonCsvtowpjson.grid(row=1,column=0,sticky='nesw')

        #bottom
        wpjsonBox = Frame(mainFrame)
        wpjsonEntry = Entry(wpjsonBox)

        buttonCopy = Button(wpjsonBox, text="copier")

        wpjsonEntry.grid(row=0,column=0)
        buttonCopy.grid(row=0,column=1)

        wpjsonBox.grid(row=2,column=0)



        mainFrame.pack()


        self.mainloop()


    




if __name__ == "__main__":
    MainView()