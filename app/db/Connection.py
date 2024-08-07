from supabase_py import create_client, Client
from models import User
from dotenv import load_dotenv
import os

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Configuración de Supabase
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Crear el cliente de Supabase
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

class Connection():

    def __init__(self, table):
        self.table = table

    # Ejemplo de escritura de datos
    def insert_user(self, user:User):
        response = supabase.table(self.table).insert({"name": user.name, "email": user.email, "last_name": user.last_name}).execute()
        if response.get("error"):
            print("Error al agregar el documento:", response["error"])
        else:
            print("Documento escrito con ID:", response["data"])
        
        return response
    
    def users(self):
        response = supabase.table(self.table).select("*").execute()

        return response

