## Challenge Data Analys
Para un correcto deploy en un entorno virtual de este proyecto, deberas seguir los siguientes pasos
### Pasos

1. Instalar la libreria venv para gestionar nuestro entorno virtual: `pip install virtualenv`
1. Dirigirse al directorio donde se desea instalar el entorno virtual y ejecutar:  
`virtualenv virtual_env_name`
1.Activar el entorno virtual: `.\virtual_env_name\Scripts\activate`
1. Una vez activado el entorno virtual proceder a instalar las dependencias:  
  `pip install requests`
  `pip install pandas`
  `pip install SQLAlchemy`
  `pip install python-decouple`
1. Comprobamos que las librerias que necesitamos esten instaladas: `pip list`
1. Con el comando cd nos posicionamos en el directorio donde se encuentre el proyecto por ejemplo `cd C:\Users\tomasr3\Desktop\aceleracion` o `cd + arrastramos la carpeta a la consola`
1. Ejecutamos los archivos .py en el siguiente orden:
`obtenciondatabases.py`
`procesamientodatos.py`
`baseadmin.py`
