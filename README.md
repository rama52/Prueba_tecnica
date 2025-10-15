# Prueba Tecnica: "Geospatial Data Developer – Agro Take-Home Challenge"

Contesto general: 
El contenido del repositorio corresponde al desarrollo de una prueba técnica descripta en este repositorio (https://github.com/cambium-earth/agtech-gdd-test?tab=readme-ov-file).

En este repositrio podemos encontrar:

-Configuración del entorno Dockerizado y pasos para configurarlo (aqui)
-Conjunto de scripts para gestionar datos y cargarlos en una base de datos
-Cuadernos Jupyter para realizar el preprocesamiento y Postprocesamiento de los datos espaciales

Parte 1. Configuración de la infraestructura con Docker y carga de los datos:
-Se creó un entorno basado en Docker Compose para el desarrollo del proyecto. Este entorno, esta compuesto por una base de datos PostgreSQL(v16) donde se le instalo la extensión PostGIS(v3.5) y la extensión h3-pg (Uber), y cuenta con un contenedor de Python 3.9 y sus principales dependencias espaciales.
-La carga de los datos a la base de datos se realizo por medio de un script en Python que se ejecuta por consola.

Parte 2.Análisis de los datos: pre y posprocesamiento
-Preprocesamiento: por fuera del entorno dockerizado se realizo una exploracion y preparacion de la informacion espacial. En esta etapa, se hiso uso de las herramientas de QGIS para la inspeccion visual y Rmarckdown para la validacion y limpieza de datos.
-Posprocesamiento: se utilizan los datos cargados en la Base de datos y se utiliza Jupyter Notebook para analizar los conjuntos de datos y crear visualizaciones. 

Estructura de archivos del repositorio: 
prueba_tecnica/
└── pt_agtech_Ramiro_Manzo/
    ├── docker-compose.yml              
    ├── REDMI.md                        
    ├── README.md                        
    │
    ├── postgis_h3/                     
    │   ├── Dockerfile
    │   └── para_el_redmi.txt           
    │
    ├── python_geo/                     
    │   ├── Dockerfile
    │   └── Preprocesamiento/
    │       ├── altimetry_kriging.geojson
    │       ├── ec_subsurface_kriging.geojson
    │       ├── ec_surface_kriging.geojson
    │       ├── Grid_final.geojson
    │       ├── preprocessing.pdf
    │       └── preprocessing.Rmd
    │
    ├── workspace/                      
    │   ├── notebooks/
    │   │   ├── Bonus.ipynb
    │   │   ├── posprocessing.ipynb
    │   │   └── Preguntas_finales.ipynb
    │   │
    │   └── scripts/
    │       └── load_data.py           
    │
    └── data/                           
        ├── Grid_final.geojson
        ├── la_magdalena_L4.geojson
        ├── soy_performance_2019_2021_2023.geojson
        └── veris_data.gpkg


