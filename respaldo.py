import psycopg2
import datetime
import os

# Configuración de conexión a la base de datos
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'nombre_de_tu_bd'
DB_USER = 'tu_usuario'
DB_PASS = 'tu_contraseña'
# Configuración de la carpeta donde se guardarán los backups
BACKUP_DIR = '/backups/'

# Nombre del archivo de backup
BACKUP_FILENAME = f"{DB_NAME}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.backup"

# Comando para hacer backup
BACKUP_COMMAND = f"pg_dump -Fc -h {DB_HOST} -p {DB_PORT} -U {DB_USER} -f {os.path.join(BACKUP_DIR, BACKUP_FILENAME)} {DB_NAME}"

# Ejecución del comando
os.system(BACKUP_COMMAND)

# Mensaje de confirmación
print("Backup completado con éxito.")