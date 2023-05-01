
# Script de respaldo automático en PostgreSQL

Este script en Python permite realizar respaldos automáticos de una base de datos en PostgreSQL utilizando el comando pg_dump.

## Requisitos Previos

- Antes de utilizar este script, asegúrese de que:

1. PostgreSQL está instalado y configurado en su sistema.
2. Tiene acceso a la base de datos que desea respaldar con un usuario con permisos suficientes para realizar el respaldo..

## Instalación y Configuración

1. Descargue el archivo respaldo.py en su sistema.
2. Abra el archivo y establezca las credenciales de acceso a la base de datos en las siguientes líneas
3. Para cargar las variables de entorno desde el archivo .env, podemos usar la librería python-dotenv. Para usarla, debemos instalarla primero usando pip:
   "pip install python-dotenv"
4. Establezca la ruta donde se guardarán los archivos de respaldo en la siguiente línea:
5. Guarde y cierre el archivo.

## Instrucciones de Uso

Pasos necesarios para utilizar el proyecto.

Para utilizar el script de respaldo automático en PostgreSQL, siga estos pasos:

1. Abra la terminal en su sistema.
2. Vaya al directorio donde se encuentra el archivo respaldo.py.
3. Ejecute el comando python respaldo.py.
4. El script generará un archivo de respaldo en la ruta especificada en BACKUP_PATH.
Puede ajustar la frecuencia de ejecución del script utilizando el programador de tareas (crontab) en Linux. Por ejemplo, para ejecutar el script todos los días a las 11:00 PM, agregue la siguiente línea en su archivo de crontab:
  0 23 * * * /usr/bin/python /ruta/al/archivo/respaldo.py



