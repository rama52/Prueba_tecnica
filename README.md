## General Context

This repository contains the development of a technical test described [here](https://github.com/cambium-earth/agtech-gdd-test?tab=readme-ov-file).

In this repository you will find:

* **Dockerized** environment configuration and usage instructions.
* Set of *scripts* for data management and database loading.
* Interactive notebooks (Jupyter and R Markdown) for preprocessing and postprocessing spatial data.

---

## Part 1. Infrastructure Setup with Docker and Data Loading

### Infrastructure

* A **Docker Compose** based environment was created for project development. This environment **consists of**:
    * A **PostgreSQL (v16)** database with installed extensions **PostGIS (v3.5)** and **h3-pg (Uber)**.
    * A **Python 3.9** container with its main spatial dependencies.
* Data loading into the database was **performed** through a Python *script* that runs via console.

---

## Part 2. Data Analysis: Pre and Postprocessing

### Preprocessing

* Outside the Dockerized environment, spatial data exploration and preparation was **performed**.
* At this stage, **QGIS** tools were used for visual inspection and **R Markdown** for data validation and cleaning.

### Postprocessing

* Data loaded in the database is utilized.
* **Jupyter Notebook** is used to analyze datasets, perform advanced spatial analysis, and create visualizations.

# Repository File Structure:
```bash
pt_agtech_Ramiro_Manzo/
├── docker-compose.yml
├── README.md

├── postgis_h3/
│   ├── Dockerfile

├── python_geo/
│   ├── Dockerfile
│   └── Preprocesamiento/
│       ├── altimetry_kriging.geojson
│       ├── ec_subsurface_kriging.geojson
│       ├── ec_surface_kriging.geojson
│       ├── Grid_final.geojson
│       ├── preprocessing.pdf
│       └── preprocessing.Rmd

├── workspace/
│   ├── notebooks/
│   │   ├── posprocessing.ipynb
│   │   └── Preguntas_finales.ipynb
│   │
│   └── scripts/
│       └── load_data.py
│   └── README.md 

└── data/
    ├── Grid_final.geojson
    ├── la_magdalena_L4.geojson
    ├── soy_performance_2019_2021_2023.parquet
    └── veris_data.gpkg



