import sqlite3 as sq

def enregistrer_utilisateur():
    req= "insert into utilisateurs(nom_complet,mot_de_passe ,email,sexe) values ("