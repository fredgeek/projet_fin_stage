from tkinter import *
from tkinter.font import Font
class gest_stats:

    def __init__(self,root,width,height):

        self.width=width
        self.height=height
################### ouverture du canvas qui va contenir la page #######################
        self.page =Canvas(root,width=self.width,height=self.height,bg="#444444")
        self.font= Font(family="helvetica",underline=True,slant="italic",weight="bold",size=24)
        Label(self.page, text="Voici vos statistiques du moment:"
              ,font=self.font,bg="#444444").place(x=self.width/2- 350,y=10)
        ###################### creation du premier frame client ##############################
        Label(self.page,text="Clients :",font=self.font,bg="#444444").place(x=self.width/4 -170,y=self.height/4)
        nombreClients = 6
        new=Frame(self.page,relief=SUNKEN,bd=1)

        Label(new,text="vous avez actuellement enregistrez \n"+str(nombreClients)+"\n client(s)"
              ,font=("arial",16,"bold")).pack(anchor=CENTER)

        new.place(x=self.width/4 -250,y=self.height/3)
        #########################  creation du frame employes  #########################

        Label(self.page, text="Employers :", font=self.font, bg="#444444").place(x=self.width / 2 +50, y=self.height / 4)
        nombre_employes = 7
        emploi= Frame(self.page, relief=SUNKEN, bd=1)

        Label(emploi, text="vous avez actuellement  enregistrez\n" + str(nombre_employes) + "\n employer(s)"
              , font=("arial", 16, "bold")).pack(anchor=CENTER)

        emploi.place(x=self.width / 2, y=self.height / 3)

        #######################  creation du frame evenements  ###############################

        Label(self.page, text="Evénements :", font=self.font, bg="#444444").place(x=self.width /4 -170, y=self.height/2 +50)
        nombre_event = 10
        test = Frame(self.page, relief=SUNKEN, bd=1)

        Label(test, text="vous avez actuellement enregistrez \n" + str(nombre_event) + "\n évenement(s)"
              , font=("arial", 16, "bold")).pack(anchor=CENTER)

        test.place(x=self.width /4 -250, y=self.height /2 +100)

##################################  cration du frame des transactions  ############################

        Label(self.page, text="Transactions :", font=self.font, bg="#444444").place(x=self.width / 2 +50 ,
                                                                                  y=self.height / 2 + 50)
        nombre_transact = 20
        test = Frame(self.page, relief=SUNKEN, bd=1)

        Label(test, text="vous avez actuellement effectuer \n" + str(nombre_transact) + "\n transaction(s)"
              , font=("arial", 16, "bold")).pack(anchor=CENTER)

        test.place(x=self.width / 2 , y=self.height/2 +100 )




        self.page.place(x=200,y=51)
