import psycopg2

def conectar():
    try:
        conexion = psycopg2.connect(
            host="localhost",
            database="Bd_Escuela",
            user="postgres",
            password="1234",
            port="5432"
        )
        return conexion
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

# Ejecutar solo si se llama directamente el archivo
if __name__ == "__main__":
    conexion = conectar()
    if conexion:
        print("Conexión exitosa a la base de datos.")
        conexion.close()
    else:
        print("💀💀💀💀💀💀 No se pudo establecer la conexión.")
