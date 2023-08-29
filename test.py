from backend.requests_db import *

# params = (12,"lucien","luc1234","fhrn@gmail.com","8578484","feminin")
# request = "insert into User values(?,?,?,?,?,?)"

# try:
#     data = set_execute_request_with_params(request,params)
#     print("Utilisateur ajoute avec succes !")
# except Exception as e:
#     print('Erreur :',e)
    

data = get_execute_request_without_params("select * from User")

print("All username : ",data[0][1])

