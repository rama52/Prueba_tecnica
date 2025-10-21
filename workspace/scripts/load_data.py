# Descripción: Carga automáticamente archivos espaciales a PostGIS
# Compatible con: .geojson, .gpkg, .parquet

import os
import geopandas as gpd
import pandas as pd
from sqlalchemy import create_engine

# ----------------------------------------
# Conexión a la base de datos
# ----------------------------------------
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

# Funciones de carga

def load_geojson(file_path, table_name):
    gdf = gpd.read_file(file_path)
    gdf.to_postgis(table_name, con=engine, if_exists="replace", index=False)
    print(f"✅ '{table_name}' cargado correctamente desde GeoJSON.")

def load_gpkg(file_path):
    layers = gpd.io.file.fiona.listlayers(file_path)
    for layer in layers:
        gdf = gpd.read_file(file_path, layer=layer)
        table_name = f"{os.path.splitext(os.path.basename(file_path))[0]}_{layer}"
        gdf.to_postgis(table_name, con=engine, if_exists="replace", index=False)
        print(f"✅ Capa '{layer}' cargada como tabla '{table_name}' desde GPKG.")

def load_parquet(file_path, table_name):
    try:
        # Intentar cargar como GeoParquet
        gdf = gpd.read_parquet(file_path)
        if "geometry" in gdf.columns or isinstance(gdf, gpd.GeoDataFrame):
            gdf.to_postgis(table_name, con=engine, if_exists="replace", index=False)
            print(f"✅ '{table_name}' cargado correctamente como GeoParquet.")
        else:
            # Si no tiene geometría, cargar como tabla normal
            df = pd.read_parquet(file_path)
            df.to_sql(table_name, con=engine, if_exists="replace", index=False)
            print(f"✅ '{table_name}' cargado correctamente como tabla Parquet.")
    except Exception as e:
        print(f"Error cargando '{file_path}': {e}")

# Recorrer carpeta y cargar archivos
for filename in os.listdir(DATA_FOLDER):
    file_path = os.path.join(DATA_FOLDER, filename)
    name, ext = os.path.splitext(filename.lower())

    if ext == ".geojson":
        load_geojson(file_path, name)
    elif ext == ".gpkg":
        load_gpkg(file_path)
    elif ext == ".parquet":
        load_parquet(file_path, name)
    else:
        print(f"Archivo '{filename}' ignorado (no soportado).")

print("Todos los archivos compatibles fueron cargados correctamente a la base de datos.")
