import os
import pandas as pd
import geopandas as gpd
from sqlalchemy import create_engine

# -----------------------------
# 1️⃣ Conexión a PostgreSQL/PostGIS
# -----------------------------
db_user = os.environ.get("POSTGRES_USER", "postgres")
db_pass = os.environ.get("POSTGRES_PASSWORD", "postgres")
db_host = os.environ.get("POSTGRES_HOST", "db")
db_port = os.environ.get("POSTGRES_PORT", 5432)
db_name = os.environ.get("POSTGRES_DB", "agtech_db")

engine = create_engine(f"postgresql+psycopg2://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}")

# -----------------------------
# 2️⃣ Definir carpeta de datos
# -----------------------------
data_folder = "/data"  # dentro del contenedor

if not os.path.exists(data_folder):
    raise FileNotFoundError(f"La carpeta {data_folder} no existe")

# -----------------------------
# 3️⃣ Cargar archivos y guardar en la base de datos
# -----------------------------
# 3a. KML
kml_path = os.path.join(data_folder, "la_magdalena_L4.kml")
if os.path.exists(kml_path):
    gdf_kml = gpd.read_file(kml_path, driver="KML")
    gdf_kml.to_postgis("la_magdalena_L4", con=engine, if_exists="replace", index=False)
    print("✅ KML cargado correctamente: la_magdalena_L4")
else:
    print(f"❌ No se encontró {kml_path}")

# 3b. GeoPackage
gpkg_path = os.path.join(data_folder, "veris_data.gpkg")
if os.path.exists(gpkg_path):
    gdf_gpkg = gpd.read_file(gpkg_path)
    # Si tiene varias capas, cargamos todas
    layers = gpd.io.file.fiona.listlayers(gpkg_path)
    for layer in layers:
        gdf_layer = gpd.read_file(gpkg_path, layer=layer)
        gdf_layer.to_postgis(layer, con=engine, if_exists="replace", index=False)
        print(f"✅ GeoPackage cargado correctamente: {layer}")
else:
    print(f"❌ No se encontró {gpkg_path}")

# 3c. Parquet
parquet_path = os.path.join(data_folder, "soy_performance_2019_2021_2023.parquet")
if os.path.exists(parquet_path):
    df_parquet = pd.read_parquet(parquet_path)  # requiere pyarrow o fastparquet
    df_parquet.to_sql("soy_performance", con=engine, if_exists="replace", index=False)
    print("✅ Parquet cargado correctamente: soy_performance")
else:
    print(f"❌ No se encontró {parquet_path}")

print("🎯 Proceso finalizado")
