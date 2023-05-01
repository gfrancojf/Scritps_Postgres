import os
import subprocess
import datetime
from dotenv import load_dotenv

# Cargar variables de entorno desde archivo .env
load_dotenv()

# Obtener valores de las variables de entorno
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
BACKUP_PATH = os.getenv("BACKUP_PATH")


# Nombre del archivo de backup
BACKUP_FILENAME = f"{DB_NAME}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.backup"

# Comando para generar el respaldo de la base de datos
backup_command = f"pg_dump -h {DB_HOST} -p {DB_PORT} -U {DB_USER} {DB_NAME} > {BACKUP_PATH, BACKUP_FILENAME}/{DB_NAME}.sql"

# Ejecutar el comando
subprocess.run(backup_command, shell=True)