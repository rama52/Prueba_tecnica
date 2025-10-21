# Environment Setup: Dockerized Geospatial Infrastructure

This section describes the **architecture** and **necessary steps** to launch the project's geospatial development and analysis environment using **Docker Compose**.

---

## 1. Geospatial Stack Architecture

To handle spatial data and ensure analysis reproducibility, an environment was created consisting of **two interconnected services**:  
one for the **geospatial database** and another for **Python-based analysis**.

---

### Database (`db`)

| **Component** | **Version / Extension** | **Main Use** |
|--------------|-------------------------|--------------|
| PostgreSQL   | v16                     | Secure and persistent data storage. |
| PostGIS      | v3.5                    | Native functions for geometry manipulation and queries. |
| H3-PG (Uber) | —                       | Extension for scalable hexagonal grid analysis (H3). |

---

### Analysis Environment (`python`)

| **Component** | **Version** | **Libraries and Tools** |
|--------------|-------------|-------------------------|
| Python       | 3.9         | GDAL, GEOS, PROJ (natively configured). |
| Tools        | JupyterLab  | GeoPandas, Shapely, Fiona, Rasterio, PyProj, GeoPy, Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, psycopg2, Folium, Leafmap. |

---

## 2. Network Configuration and Communication

The containers are managed through a single **`docker-compose.yml`** file, which:

- Builds images from their respective **Dockerfile**.  
- Maintains an **internal work network (`geo_network`)** for secure communication between containers.  
- Defines **environment variables** in the Python container to facilitate database connection  
  (e.g.: `POSTGRES_HOST=db`).  

---
## 
## 3. Quick Start Guide

### 3.1. Build the Images

### Before launching the stack for the first time, run:

```bash
docker-compose build
```
###  3.2. Launch the Full Stack

```bash
docker-compose up -d
```

### This will start both services:

| Service   | Description                                                    | Connection                                                      |
|-----------|----------------------------------------------------------------|-----------------------------------------------------------------|
| **db**    | Container with PostGIS ready for spatial analysis.             | Persistent data in `pgdata/`                                    |
| **python**| Container with Python 3.9 + JupyterLab and geospatial libraries.| The local folder `./workspace` is mounted inside the container. |

### 3.3. Access the Database (psql)
- To access the database inside the container (e.g., to check tables or installed extensions):

```bash
docker exec -it pg_geo psql -U postgres -d agtech_db

```
### 3.4. Access the JupyterLab Environment

### Open your browser and go to: http://localhost:8888

### From there you can work on the notebooks mounted in the workspace/notebooks/ directory.

