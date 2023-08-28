from tkinter import *
from time import strftime
from pages.Gestion_des_clients.show_cutomer import all_clients
from pages.Gestion_des_employés.all_employee import all_employer
from pages.Gestion_des_finance.all_spending import all_spending
from pages.Gestion_des_finance.new_spending import ajout_facture

from pages.Gestion_des_employés.add_employee import ajout_employer
from pages.Gestion_des_employés.delet_employee import delete_employer
from pages.Gestion_des_clients.Add_customer import ajout_clients
from pages.Gestion_des_clients.delet_customer import delete_clients
from pages.Gestion_des_statistiques.stat_de_entreprise import Nbr_clients
from pages.Gestion_des_activités.add_event import add_event
from pages.Gestion_des_activités.delet_event import delete_event
from pages.Gestion_des_activités.show_events import all_event
from pages.Gestion_des_statistiques.gestion_stats import gest_stats
from pages.home.boutton_compte import mon_compte


class HomePage:

    def __init__(self,root,width,height):
        # dimensions de la fenetre
        self.width = width
        self.height = height


################### root = fenetre parent, width et height sont les dimensions de la fenetre #############################
        self.page = Canvas(root,width=self.width,height=self.height,bg="yellow")

    ################# barre de présentation en haut ########################
        self.presentationPart = Canvas(self.page,width=self.width,height=50,bg="#32a852")
        username= "yac "
        Label(self.presentationPart,text="Bienvenue Mr. "+username+" dans votre espace perso",font=("Arial",28,"italic"),bg="#32a852").place(x=300,y=7)




        self.presentationPart.place(x=0,y=0)

    ##################    fin de la barre de presentation  ################################

        from pages.authentication.login_page import LoginPage

    ########## menus des fonctionnalités  #####################

        self.fonction = Canvas(self.page,width=200,height=self.height-51,bg="blue")

        ############### creation du bouton mon compte  #####################
        Button(self.fonction, text=" Mon Compte", bg="blue"
               , width=13, height=1, fg="black",font=("arial",14,"bold"),bd=0
               ,activebackground="blue"
               ,activeforeground="white",command=lambda : mon_compte(self.page,self.width,self.height)).place(x=15, y=12)

        ########## creation du menu des finances  ###########################

        menu_des_finances=Menubutton(self.fonction, text=" Finances "
               , bg="blue", width=13, height=1, fg="black",font=("arial",14,"bold")
                                     ,activebackground="blue",activeforeground="white")
        menu = Menu(menu_des_finances, tearoff=0)
        menu_des_finances["menu"] = menu
        menu.add_command(label="Ajout.Facture",activebackground="blue",activeforeground="white"
                         ,command= lambda: ajout_facture(self.page,self.width,self.height))
        #menu.add_command(label="suppr.Facture")
        menu.add_command(label="List.Facture",activebackground="blue",activeforeground="white"
                         ,command=lambda:all_spending(self.page,self.width,self.height))
        menu_des_finances.place(x=4, y=245)

        #############  creation du bouton des employers   #################

        menu_des_employers= Menubutton(self.fonction, text=" Mes Employers ",relief=FLAT
             , bg="blue", width=13, height=1, fg="black",font=("arial",14,"bold"),activebackground="blue"
                                       ,activeforeground="white")
        menu= Menu(menu_des_employers,tearoff=0)
        menu_des_employers["menu"]= menu
        menu.add_command(label="Ajout.Employer",activebackground="blue",activeforeground="white"
                         ,command = lambda :ajout_employer(self.page,self.width,self.height))
        menu.add_command(label="suppr:employer",activebackground="blue",activeforeground="white"
                         ,command = lambda :delete_employer (self.page,self.width,self.height))
        menu.add_command(label="List.Employer",activebackground="blue",activeforeground="white"
                         ,command = lambda :all_employer (self.page,self.width,self.height))
        menu_des_employers.place(x=25, y=70)

        ################# creation du menu des evènements #################

        menu_des_evenements=Menubutton(self.fonction, text=" Évenements "
               , bg="blue", width=13, height=1, fg="black",font=("arial",14,"bold")
                                       ,activebackground="blue",activeforeground="white")
        menu= Menu(menu_des_evenements,tearoff=0)
        menu_des_evenements["menu"] = menu
        menu.add_command(label="Ajout.rendez-Vous",activebackground="blue"
                         ,activeforeground="white",command=lambda:add_event(self.page,self.width,self.height))
        menu.add_command(label="Suppr.rendez-Vous",activebackground="blue"
                         ,activeforeground="white",command=lambda:delete_event(self.page,self.width,self.height))
        menu.add_command(label="List.rendez-Vous",activebackground="blue"
                         ,activeforeground="white",command=lambda:all_event(self.page,self.width,self.height))
        menu_des_evenements.place(x=12, y=130)

        ############### creation du menus des clients #####################
        menu_des_clients=Menubutton(self.fonction, text=" Clients "
               , bg="blue", width=13, height=1, fg="black",font=("arial",14,"bold"),activebackground="blue",activeforeground="white")
        menu= Menu(menu_des_clients,tearoff=0)
        menu_des_clients["menu"]=menu
        menu.add_command(label="Ajout.Clients",activebackground="blue"
                         ,activeforeground="white",command= lambda :ajout_clients(self.page,self.width,self.height))
        menu.add_command(label="Suppr.Clients",activebackground="blue"
                         ,activeforeground="white",command= lambda :delete_clients(self.page,self.width,self.height))
        menu.add_command(label="List.Clients",activebackground="blue"
                         ,activeforeground="white",command= lambda :all_clients(self.page,self.width,self.height))
        menu_des_clients.place(x=4, y=185)

        ############## creation du menu des statistiques  ###################
        menu_des_statistiques=Button(self.fonction, text=" Statistiques "
               , bg="blue", width=13, height=1, fg="black", font=("arial", 14, "bold"),relief=FLAT
                                     ,activebackground="blue",activeforeground="white",command=lambda:gest_stats(self.page,self.width,self.height))
        #menu = Menu(menu_des_statistiques, tearoff=0)
        #menu_des_statistiques["menu"] = menu
        #menu.add_command(label="Nbre.Employes",activebackground="blue",activeforeground="white",command=lambda:Nbr_employer(self.page,self.width,self.height))
        #menu.add_command(label="Nbre.Clients",activebackground="blue",activeforeground="white",command=lambda:Nbr_clients(self.page,self.width,self.height))
        #menu.add_command(label="Nbre.Transactions",activebackground="blue",activeforeground="white",command=lambda:Nbr_transactions(self.page,self.width,self.height))
        #menu.add_command(label="Nbre.Evenements",activebackground="blue",activeforeground="white",command=lambda:Nbr_evenements(self.page,self.width,self.height))
        menu_des_statistiques.place(x=4, y=310)

        #creation du bouton se deconnecter
        Button(self.fonction, text=" se deconnecter ",bg="blue",bd=0,width=13,height=1,fg="red"
               ,command =lambda: LoginPage(self.page,self.width,self.height),activebackground="blue"
               ,activeforeground="white",font=("arial",14,"italic")).place(x=6,y=self.height-100)
        self.fonction.place(x=0,y=51)
    ############ fin de la barre des fonctionnalités #########################

########### place de presentation des fonctionnalités #########################
        self.img = PhotoImage(file="accueil-entreprise.png").zoom(25).subsample(13)
        self.present = Canvas(self.page,width=self.width-200,height=self.height-51,bg="aqua")
        Label(self.present, image=self.img).place(x=0,y=0)



        self.present.place(x=200,y=51)
######### fin du menu de presentation des fnctionnalités #######################

      #  Label(self.page,text="Home page").place(x=40,y=20)

        #bouton de transition ver le register_page
        #Button(
         #   self.page, text="Back button ",
          #     command=self.page.destroy).place(x=90,y=60)


        self.page.place(x=0,y=0)


