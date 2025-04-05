Proyecto_2 
Nahir Ayelen Piancazza 24634/2

Ejercicio 10
Este proyecto muestra los resultados de varias rondas, generando clasificaciones y seleccionando a los MVPs según su puntaje, permitiendo evaluar el desempeño del equipo.

Estructura del Código
Las funciones necesarias están dentro del directorio src, mientras que los notebooks se encuentran en la carpeta notebooks.

Instalación de Dependencias
Para ejecutar el proyecto, es recomendable crear un entorno virtual e instalar las librerias necesarias.

Crear un entorno virtual
Siguiendo la convención, el entorno virtual se almacena dentro del repositorio del proyecto. Para generarlo, usa el siguiente comando:

python -m venv venv
Explicación del comando:
python -m → Ejecuta un módulo de Python.
venv → Módulo que permite crear entornos virtuales.
venv → Nombre del directorio donde se guardará el entorno.
Activar y desactivar el entorno virtual

En Windows:
source venv\Scripts\activate

En macOS/Linux:
source venv/bin/activate

Para salir del entorno virtual, ejecuta:
deactivate
Instalar las dependencias
Dentro del proyecto, ejecuta el siguiente comando en la terminal:
pip install -r requirements.txt

Si el archivo requirements.txt no existe, puedes generarlo con:
pip freeze > requirements.txt

Ejecución del Proyecto
Desde notebook, primero asegúrate de estar dentro del entorno virtual y luego abre Jupyter Notebook con:

jupyter notebook
Desde Jupyter, navega hasta la carpeta notebooks y selecciona el archivo correspondiente.
Estructura del Proyecto

Proyecto_2/
│── notebooks/             # Directorio de notebooks
│   ├── ejercicio10.ipynb  # Archivo principal del ejercicio
│── src/                   # Carpeta con los módulos de Python
│   ├── __init__.py        # Indica que es un paquete
│   ├── funciones.py       # Archivo con las funciones principales
│── requirements.txt       # Lista de dependencias del proyecto
│── README.md              # Documentación e instrucciones
Este proyecto permite analizar el rendimiento del equipo a lo largo de múltiples rondas, identificando el jugador más valioso en cada una. 
