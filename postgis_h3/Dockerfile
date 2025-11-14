### ETAPA 1: BUILDER (Compilación de H3 y h3-pg) ###

FROM postgis/postgis:16-3.5 AS builder

# Instalar dependencias necesarias para COMPILAR
RUN apt-get update && apt-get install -y --no-install-recommends \
    git build-essential cmake libssl-dev pkg-config ca-certificates \
    libpq-dev postgresql-server-dev-16 \
 && rm -rf /var/lib/apt/lists/*

# Instalar la librería base H3 (versión estable v4.1.0)
RUN git clone --branch v4.1.0 https://github.com/uber/h3.git /tmp/h3 \
 && cd /tmp/h3 && mkdir build && cd build \
 && cmake -DBUILD_SHARED_LIBS=ON .. \
 && make -j$(nproc) && make install \
 && ldconfig && rm -rf /tmp/h3

# Instalar h3-pg (extensión PostgreSQL oficial v4.2.3)
RUN git clone --branch v4.2.3 https://github.com/bytesandbrains/h3-pg.git /tmp/h3-pg \
 && cd /tmp/h3-pg && mkdir build \
 && cd build \
 && cmake -DCMAKE_BUILD_TYPE=Release .. \
 && make && make install \
 && rm -rf /tmp/h3-pg

### ETAPA 2: FINAL (Runtime - Imagen de Ejecución Limpia) ###
# Solo contiene la imagen base de PostGIS + los binarios necesarios.

FROM postgis/postgis:16-3.5

# Copiar archivos de librería de H3 y la extensión h3-pg compilados
# Nota: Las rutas son las estándar de instalación para PostgreSQL 16.
COPY --from=builder /usr/local/lib/libh3.so /usr/local/lib/
COPY --from=builder /usr/lib/postgresql/16/lib/h3.so /usr/lib/postgresql/16/lib/
COPY --from=builder /usr/share/postgresql/16/extension/h3--*.sql /usr/share/postgresql/16/extension/
COPY --from=builder /usr/share/postgresql/16/extension/h3.control /usr/share/postgresql/16/extension/

EXPOSE 5432
