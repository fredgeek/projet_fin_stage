from backend.requests_db import *
import random as rd 
# params = (12,"lucien","luc1234","fhrn@gmail.com","8578484","feminin")
# request = "insert into User values(?,?,?,?,?,?)"

# try:
#     data = set_execute_request_with_params(request,params)
#     print("Utilisateur ajoute avec succes !")
# except Exception as e:
#     print('Erreur :',e)
    
# generateur d' id
id = rd.randint(100,900) +  rd.randint(1,9) +  rd.randint(10,90)

