from models import user
from config.supabasedb import supabase

class UserDb():

    def __init__(self, table):
        self.table = table

    def insert_user(self, user:user):
        response = supabase.table(self.table).insert({"name": user.name, "email": user.email, "last_name": user.last_name}).execute()
        if response.get("error"):
            print("Error al agregar el documento:", response["error"])
        else:
            print("Documento escrito con ID:", response["data"])
        
        return response
    
    def users(self):
        response = supabase.table(self.table).select("*").execute()

        return response

