# Django-api
 
# Installacion de django API

1.Installar python
https://www.python.org/downloads/ 

opcional
https://docs.python.org/3/tutorial/venv.html
 Es recomendado usar venv o Virtual Environment para installar django y los archivos de este proyecto para que queden aparte y no sean afectados por otros posibles packetes ya instalados en el computador.

en powershell, cdm o cli
 
Para crear un entorno virtual, decide en qué directorio deseas colocarlo y ejecuta el módulo `venv` como un script con la ruta del directorio:

```bash
python -m venv tutorial-env
```

Esto creará el directorio `tutorial-env` si no existe, y también creará directorios dentro de él que contienen una copia del intérprete de Python y varios archivos de soporte.

Una ubicación común para un entorno virtual es `.venv`. Este nombre mantiene el directorio típicamente oculto en tu shell y, por lo tanto, fuera del camino, mientras le da un nombre que explica por qué existe el directorio. También evita conflictos con archivos de definición de variables de entorno `.env` que algunas herramientas soportan.

Una vez que hayas creado un entorno virtual, puedes activarlo.

En Windows, ejecuta:

```bash
tutorial-env\Scripts\activate
```

con esto en la consola deveria verse el nombre del venv antes del directorio

2. instalar los componentes

 descargar el archivo requirements.txt

 y usar el commando
 ```bash
pip install -r .\requirements.txt
```
esto comenzara a installar todos los componentes usados para el backend

3. descargar proyecto

luego descargar la carpeta DjangoAPI

5. activar el proyecto

dentro de la carpeta de DjangoAPI usar:
```bash
...\> py manage.py runserver
```
esto hara que el servidor de API quede funcionado

## Postman
Ejemplos de las respuestas de la API se encuentran en este directorio:
-> DjangoAPI/Api json responces

## Usando el API con postman 

todas las tablas de la base de datos funcionan con el API pero para esta activadad como ejemplo usaremos:
artist
album
song
la url para usar la API es:  [localhost]/api/[tabla] por ejemplo : http://127.0.0.1:8000/api/artist 

si se quiere utilar la informacion de un solo objeto se incluye el id en la url: http://127.0.0.1:8000/api/artist/16


