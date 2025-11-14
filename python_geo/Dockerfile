### ETAPA 1: BUILDER (Compilación y Preparación de Entorno) ###

FROM python:3.11-slim-bookworm AS builder

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    gdal-bin libproj25 proj-data proj-bin \
    libgeos-dev libsqlite3-mod-spatialite libpq5 \
    wget curl ca-certificates \
 && apt-get clean && rm -rf /var/lib/apt/lists/*


ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal
ENV GDAL_DATA=/usr/share/gdal
ENV PROJ_LIB=/usr/share/proj

RUN pip install --no-cache-dir --upgrade pip

# Librerías Python
RUN pip install --no-cache-dir \
    earthengine-api==0.1.419 \
    google-api-python-client==2.138.0 \
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
    libpysal==4.8.1 \
    esda==2.5.1 \
    contextily==1.6.2 \
    pyarrow==17.0.0 \
    rasterstats==0.19.0 \
    h3==3.7.6   # ← Hexágonos Uber H3


### ETAPA 2: FINAL (Runtime) ###

FROM python:3.11-slim-bookworm

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    gdal-bin libproj25 proj-data proj-bin \
    libgeos-dev libsqlite3-mod-spatialite libpq5 \
    wget curl ca-certificates \
 && apt-get clean && rm -rf /var/lib/apt/lists/*

ENV GDAL_DATA=/usr/share/gdal
ENV PROJ_LIB=/usr/share/proj

COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages

# Copia los ejecutables (como 'jupyter')
COPY --from=builder /usr/local/bin/ /usr/local/bin/

# assets de JupyterLab
COPY --from=builder /usr/local/share/jupyter/ /usr/local/share/jupyter/

WORKDIR /workspace
COPY . /workspace

EXPOSE 8888

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--no-browser", "--allow-root", "--NotebookApp.token=''", "--NotebookApp.password=''"]