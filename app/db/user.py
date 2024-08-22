from config.supabasedb import supabase
from models.userPayload import UserPayload

class UserDb():

    def __init__(self, table):
        self.table = table
        self.table_user = supabase.table(self.table)

    def insert_user(self, user:UserPayload):

        response = self.table_user.insert(user.to_dict()).execute()
        if response.get("error"):
            print("Error al agregar el documento:", response["error"])
        else:
            print("Documento escrito con ID:", response["data"])
        
        return response
    
    def users(self):
        response = self.table_user.select("*").execute()

        return response
    
    def user_by_id(self, id:int):
        return self.table_user.select("*").eq("id", str(id)).execute()
    
    def user_delete(self, id):
        response = {}
        res = self.user_by_id(int(id))
        if res["data"]:
            response = self.table_user.delete().eq("id", str(id)).execute()
        else:
            response["data"] = "Usuario no existe"
            response["code"] = 404         

        return response
    
    def user_update(self, user:UserPayload, id: int):

        response = self.table_user.update(user.to_dict()).eq("id", str(id)).execute()

        if response["data"]:
            response["message"] = "User updated successfully"
        else:
            response["message"] = "The user could not update"

        return response