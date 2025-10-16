# Configuración del Entorno: Infraestructura Geoespacial Dockerizada

Esta sección describe la **arquitectura** y los **pasos necesarios** para levantar el entorno de desarrollo y análisis geoespacial del proyecto utilizando **Docker Compose**.

---

## 1. Arquitectura del Stack Geoespacial

Para el manejo de datos espaciales y la reproducibilidad del análisis, se creó un entorno compuesto por **dos servicios interconectados**:  
uno para la **base de datos geoespacial** y otro para el **análisis en Python**.

---

### Base de Datos (`db`)

| **Componente** | **Versión / Extensión** | **Uso Principal** |
|----------------|--------------------------|-------------------|
| PostgreSQL     | v16                      | Almacenamiento seguro y persistente de datos. |
| PostGIS        | v3.5                     | Funciones nativas para manipulación y consulta de geometrías. |
| H3-PG (Uber)   | —                        | Extensión para análisis de grillas hexagonales escalables (H3). |

---

### Entorno de Análisis (`python`)

| **Componente** | **Versión** | **Librerías y Herramientas** |
|----------------|-------------|-------------------------------|
| Python         | 3.9         | GDAL, GEOS, PROJ (nativos configurados). |
| Herramientas   | JupyterLab  | GeoPandas, Shapely, Fiona, Rasterio, PyProj, GeoPy, Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, psycopg2, Folium, Leafmap. |

---

## 2. Configuración y Comunicación de la Red

Los contenedores se gestionan mediante un único archivo **`docker-compose.yml`**, el cual:

- Construye las imágenes a partir de sus respectivos **Dockerfile**.  
- Mantiene una **red interna de trabajo (`geo_network`)** para la comunicación segura entre contenedores.  
- Define **variables de entorno** en el contenedor de Python para facilitar la conexión a la base de datos  
  (por ejemplo: `POSTGRES_HOST=db`).  

---
## 
## 3. Guía de Uso Rápida

### 3.1. Construir las Imágenes

### Antes de levantar el stack por primera vez, ejecutá:

```bash
docker-compose build
```
###  3.2. Levantar el stack completo

```bash
docker-compose up -d
```

### Esto iniciará los dos servicios:

| Servicio   | Descripción                                                       | Conexión                                                           |
| ---------- | ----------------------------------------------------------------- | ------------------------------------------------------------------ |
| **db**     | Contenedor con PostGIS listo para análisis espaciales.            | Datos persistentes en `pgdata/`                                    |
| **python** | Contenedor con Python 3.9 + JupyterLab y librerías geoespaciales. | La carpeta local `./workspace` está montada dentro del contenedor. |

### 3.3. Acceder a la Base de Datos (psql)
- Para ingresar a la base de datos dentro del contenedor (por ejemplo, para verificar tablas o extensiones instaladas):

```bash
docker exec -it pg_geo psql -U postgres -d agtech_db

```
### 3.4. Acceder al entorno JupyterLab

### Abrí tu navegador y entrá en: http://localhost:8888

### Desde ahí podés trabajar en los notebooks montados en el directorio workspace/notebooks/.

