# Descripción: Carga automáticamente archivos espaciales a PostGIS

import os
import geopandas as gpd
from sqlalchemy import create_engine

# Conexión a la base de datos

DB_USER = os.getenv("POSTGRES_USER", "postgres")
DB_PASS = os.getenv("POSTGRES_PASSWORD", "postgres")
DB_HOST = os.getenv("POSTGRES_HOST", "db")
DB_PORT = os.getenv("POSTGRES_PORT", "5432")
DB_NAME = os.getenv("POSTGRES_DB", "agtech_db")

engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# Carpeta de datos

DATA_FOLDER = "/data"

if not os.path.exists(DATA_FOLDER):
    raise FileNotFoundError(f"La carpeta {DATA_FOLDER} no existe en el contenedor.")

# Función para cargar archivos GeoJSON

def load_geojson(file_path, table_name):
    gdf = gpd.read_file(file_path)
    gdf.to_postgis(table_name, con=engine, if_exists="replace", index=False)
    print(f"✅ '{table_name}' cargado correctamente desde GeoJSON.")

# Función para cargar archivos GPKG

def load_gpkg(file_path):
    layers = gpd.io.file.fiona.listlayers(file_path)
    for layer in layers:
        gdf = gpd.read_file(file_path, layer=layer)
        table_name = f"{os.path.splitext(os.path.basename(file_path))[0]}_{layer}"
        gdf.to_postgis(table_name, con=engine, if_exists="replace", index=False)
        print(f"✅ Capa '{layer}' cargada como tabla '{table_name}' desde GPKG.")

# Recorrer carpeta y cargar archivos automáticamente

for filename in os.listdir(DATA_FOLDER):
    file_path = os.path.join(DATA_FOLDER, filename)
    if filename.lower().endswith(".geojson"):
        table_name = os.path.splitext(filename)[0]
        load_geojson(file_path, table_name)
    elif filename.lower().endswith(".gpkg"):
        load_gpkg(file_path)
    else:
        print(f"⚠️ Archivo '{filename}' ignorado (no soportado).")

print("Todos los archivos compatibles fueron cargados correctamente a la base de datos.")
