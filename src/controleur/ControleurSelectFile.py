from tkinter.filedialog import askopenfilename

class ControleurSelectFile():

    def __init__(self,entryPath) -> None:
        self.entryPath = entryPath

    def Onclique(self,event):

        cheminFichier = askopenfilename()

        if cheminFichier != "":

            self.entryPath.entryInput.delete(0,"end")
            self.entryPath.entryInput.insert(0, cheminFichier)