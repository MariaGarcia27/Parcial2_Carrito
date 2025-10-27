from supabase import create_client
from dotenv import load_dotenv
import os

# Cargar variables del archivo .env
load_dotenv()

# Obtener las variables del .env
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Crear cliente de conexión
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Probar conexión
def test_connection():
    try:
        data = supabase.table("lecturas_luz").select("*").execute()
        print("Conexión exitosa 🎉")
        print(data)
    except Exception as e:
        print("Error al conectar con Supabase:", e)

if __name__ == "__main__":
    test_connection()
