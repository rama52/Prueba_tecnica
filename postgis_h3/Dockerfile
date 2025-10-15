# Imagen base: PostgreSQL 16 + PostGIS 3.5
FROM postgis/postgis:16-3.5

# Instalar dependencias necesarias
RUN apt-get update && apt-get install -y --no-install-recommends \
    git build-essential cmake libssl-dev pkg-config ca-certificates \
    libpq-dev postgresql-server-dev-16 \
 && rm -rf /var/lib/apt/lists/*

# Instalar la librería base H3 (versión estable)
RUN git clone --branch v4.1.0 https://github.com/uber/h3.git /tmp/h3 \
 && cd /tmp/h3 && mkdir build && cd build \
 && cmake -DBUILD_SHARED_LIBS=ON .. \
 && make -j$(nproc) && make install \
 && ldconfig && rm -rf /tmp/h3

# Instalar h3-pg (extensión PostgreSQL oficial)
RUN git clone --branch v4.2.3 https://github.com/bytesandbrains/h3-pg.git /tmp/h3-pg \
 && cd /tmp/h3-pg && mkdir build && cd build \
 && cmake -DCMAKE_BUILD_TYPE=Release .. \
 && make && make install \
 && rm -rf /tmp/h3-pg

EXPOSE 5432