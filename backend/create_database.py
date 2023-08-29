# importation des dependances...
import sqlite3
import sqlite3 as sq

#create_user = """
 #   CREATE TABLE USER IF NOT EXIST(
  #  id integer,
   # name text NOT NULL,
    
    #)
#"""

#create_employee = """
 #   CREATE TABLE USER IF NOT EXIST(
  #  id integer,
   # name text,

    #)
#""")"""


con =sq.connect("projet_stage_database.db")

cur= con.cursor()
req1="create table if not exists utilisateurs( idUtilisateur integer not null  primary key autoincrement" \
    ",nom_complet text,mot_de_passe text,email text,sexe text,) "
cur.execute(req1)
req2 = "create table if not exists evenements( idEvenement  integer not null primary key autoincrement " \
       "nom text,motif text,sexe text,lieu_rendez_vous text, status text,date_rendez_vous text,heure_rendez_vous text,contact text)"

cur.execute(req2)

req3 = "create table if not exists clients(  idClients integer not null primary key autoincrement " \
       "nom text,email text,sexe text,quartier text,ville text,secteur_activite text,,contact text)"
cur.execute(req3)

req4 = "create table  if not exists employer(  idEmployer integer not null primary key autoincrement " \
       "nom text,email text,sexe text,contact text)"
cur.execute(req4)

req5 = "create table  if not exists finances( idFinances  integer not null primary key autoincrement " \
       "date_entrez text,type text,status text,montant integer,motif text)"
cur.execute(req5)

con.commit()
con.close()