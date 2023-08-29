# importation des dependances...
import sqlite3
import sqlite3 as sq

cree_table_utilisateur = """ 
CREATE TABLE utilisateur IF NOT EXIST (
    id INTEGER  PRIMARY KEY,
    fullname text NOT NULL,
    password MOT NULL,
    email text NOT NULL, 
    phone text NOT NULL,
    gender text NOT NULL
    )"""

 
# creation de la tablet evenement
cree_table_Event = """
CREATE TABLE Event IF NOT EXIST (
    id integer  PRIMARY KEY,
    meet_with text NOT NULL,
    gender text NOT NULL,
    phone text NOT NULL,
    place text NOT NULL,
    event_status text NOT NULL,
    reason_event text NOT NULL, 
    eventdate text NOT NULL ,
    hour_event text NOT NULL 
    )"""




# creation table client
cree_table_client = """
CREATE TABLE client IF NOT EXIST (
    id integer  PRIMARY KEY,
    fullname text NOT NULL , 
    email text NOT NULL , 
    phone interger NOT NULL , 
    city text NOT NULL ,
    sector text NOT NULL ,
    gender text NOT NULL , 
    quater text NOT NULL 
    )"""



cree_table_employer = """ 
CREATE TABLE employee IF NOT EXIST (
    id integer PRIMARY KEY,
    fullname text NOT NULL ,
    email text NOT NULL ,
    phone interger NOT NULL ,
    gender text NOT NULL 
    )"""




# creation table finance
cree_table_finance = """
CREATE TABLE finance IF NOT EXIST (
    id  integer PRIMARY KEY,
    reason text NOT NULL , 
    amount integer NOT NULL,
    date text NOT NULL,
    status text NOT NULL,
    type text NOT NULL
    )"""


