## Contexto General

El contenido del repositorio corresponde al desarrollo de una prueba técnica descripta en este repositorio: [hipervínculo al repo].

En este repositorio podemos encontrar:

* Configuración del entorno **Dockerizado** y pasos para su uso (aquí).
* Conjunto de *scripts* para gestionar datos y cargarlos en una base de datos.
* Cuadernos Jupyter para realizar el preprocesamiento y el posprocesamiento de los datos espaciales.

---

## Parte 1. Configuración de la Infraestructura con Docker y Carga de los Datos

### Infraestructura

* Se creó un entorno basado en **Docker Compose** para el desarrollo del proyecto. Este entorno **está compuesto** por:
    * Una base de datos **PostgreSQL (v16)** donde **se le instaló** la extensión **PostGIS (v3.5)** y la extensión **h3-pg (Uber)**.
    * Un contenedor de **Python 3.9** y sus principales dependencias espaciales.
    * (Puede encontrar más detalles sobre esta configuración aquí: [hipervínculo]).
* La carga de los datos a la base de datos **se realizó** por medio de un *script* en Python que se ejecuta por consola.

---

## Parte 2. Análisis de los Datos: Pre y Posprocesamiento

### Preprocesamiento

* Por fuera del entorno Dockerizado **se realizó** una exploración y preparación de la información espacial.
* En esta etapa, **se hizo** uso de las herramientas de **QGIS** para la inspección visual y **RMarkdown** para la validación y limpieza de datos.

### Posprocesamiento

* Se utilizan los datos cargados en la Base de datos.
* Se emplea **Jupyter Notebook** para analizar los conjuntos de datos, ejecutar el análisis espacial avanzado y crear visualizaciones. 

# Estructura de archivos del repositorio: 
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


