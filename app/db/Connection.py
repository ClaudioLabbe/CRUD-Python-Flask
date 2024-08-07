from supabase_py import create_client, Client
from models import User

# Configuración de Supabase
SUPABASE_URL = "https://nuoygvimyznmnytuivyn.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im51b3lndmlteXpubW55dHVpdnluIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjMwNDE3MDMsImV4cCI6MjAzODYxNzcwM30.JAKTZi-SJgBhhvfONNwoh_6oex9mH-3XRdaK_7GO1n8"

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

