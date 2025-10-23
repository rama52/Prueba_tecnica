# Imagen base: Python 3.9 (estable y compatible con librerías geoespaciales)
FROM python:3.9-slim-bullseye

# Evita prompts interactivos en la instalación
ENV DEBIAN_FRONTEND=noninteractive

# Instalar dependencias del sistema necesarias para GDAL, GEOS, PROJ y Spatialite
RUN apt-get update && apt-get install -y --no-install-recommends \
    gdal-bin libgdal-dev libproj-dev proj-data proj-bin \
    libgeos-dev libspatialindex-dev libsqlite3-mod-spatialite \
    build-essential wget curl ca-certificates \
 && rm -rf /var/lib/apt/lists/*

# Variables de entorno para GDAL y PROJ
ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal
ENV GDAL_DATA=/usr/share/gdal
ENV PROJ_LIB=/usr/share/proj

# Instalar librerías Python (versiones estables y probadas)
RUN pip install --no-cache-dir \
    numpy==1.26.4 \
    pandas==2.2.2 \
    geopandas==0.14.4 \
    shapely==2.0.4 \
    rasterio==1.3.10 \
    fiona==1.9.6 \
    pyproj==3.6.1 \
    psycopg2-binary==2.9.9 \
    geopy==2.4.1 \
    matplotlib==3.9.2 \
    folium==0.17.0 \
    jupyterlab==4.2.5 \
    ipywidgets==8.1.2 \
    branca==0.7.2 \
    seaborn==0.13.2 \
    scikit-learn==1.5.1 \
    leafmap==0.31.2 \
    sqlalchemy==2.0.22 \
    # 🔽 Librerías nuevas agregadas (22-10-25)
    libpysal==4.8.1 \
    esda==2.5.1 \
    contextily==1.6.2 \
    pyarrow==17.0.0

# Crear directorio de trabajo
WORKDIR /workspace

# Exponer el puerto de JupyterLab
EXPOSE 8888

# Comando por defecto: lanzar JupyterLab sin token
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--no-browser", "--allow-root", "--NotebookApp.token=''", "--NotebookApp.password=''"]




# 🔽 Librerías nuevas agregadas
    libpysal==4.8.1 \
    esda==2.5.1 \
    contextily==1.6.2 \
    pyarrow==17.0.0

