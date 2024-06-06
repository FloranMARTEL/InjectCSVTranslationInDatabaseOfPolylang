
from model.updateTranslation import updateTranslation
from model.convertiseur import csvToWpjson


from view.Popup import Popup


import mariadb

class ControleurUpdateDatabase():

    def __init__(self,entryPath,entryUser,entryPassword,entryHost,entryPort,entryDatabase) -> None:
        self.entryPath = entryPath

        self.entryUser = entryUser
        self.entryPassword = entryPassword
        self.entryHost = entryHost
        self.entryPort = entryPort
        self.entryDatabase = entryDatabase

    def Onclique(self,event):

        
        try :

            dirrectory = self.entryPath.entryInput.get()
            langs,wpJson = csvToWpjson(dirrectory)

            user = self.entryUser.entryInput.get()
            password = self.entryPassword.entryInput.get()
            host = self.entryHost.entryInput.get()
            port = int(self.entryPort.entryInput.get())
            database = self.entryDatabase.entryInput.get()

            updateTranslation(langs,wpJson,user,password,host,port,database)

            Popup("✅ la data base à été update ✅")
        except BaseException as e :
            Popup("✘ "+ str(e) +" ✘")
        except:
            Popup("✘ Erreur Inconnu ✘")


        
