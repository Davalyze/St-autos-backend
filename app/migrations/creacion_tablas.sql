
DROP TABLE IF EXISTS origen_vehiculo_enum CASCADE;
DROP TABLE IF EXISTS estado_vehiculo_enum CASCADE;
DROP TABLE IF EXISTS vehiculos CASCADE;
DROP TABLE IF EXISTS clientes CASCADE;
DROP TABLE IF EXISTS municipios CASCADE;
DROP TABLE IF EXISTS departamentos CASCADE;
DROP TABLE IF EXISTS transmisiones CASCADE;
DROP TABLE IF EXISTS colores CASCADE;
DROP TABLE IF EXISTS combustibles CASCADE;
DROP TABLE IF EXISTS condiciones_vehiculo CASCADE;
DROP TABLE IF EXISTS marcas_vehiculo CASCADE;
DROP TABLE IF EXISTS categorias_vehiculo CASCADE;

-- ===============================
-- Tipos ENUM
-- ===============================
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'origen_vehiculo_enum') THEN
        CREATE TYPE origen_vehiculo_enum AS ENUM ('Captacion', 'Compra');
    END IF;

    IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'estado_vehiculo_enum') THEN
        CREATE TYPE estado_vehiculo_enum AS ENUM ('Activo', 'Inactivo');
    END IF;
END$$;

-- ===============================
-- Dimensiones básicas
-- ===============================

CREATE TABLE IF NOT EXISTS categorias_vehiculo (
    id          SERIAL PRIMARY KEY,
    nombre      VARCHAR(80) UNIQUE NOT NULL,
    activo      BOOLEAN NOT NULL DEFAULT TRUE,
    created_at  TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS marcas_vehiculo (
    id              SERIAL PRIMARY KEY,
    nombre          VARCHAR(80) NOT NULL,
    categoria_id    INTEGER NOT NULL REFERENCES categorias_vehiculo(id),
    activo          BOOLEAN NOT NULL DEFAULT TRUE,
    created_at      TIMESTAMP NOT NULL DEFAULT NOW(),
    UNIQUE (nombre, categoria_id)
);

CREATE TABLE IF NOT EXISTS condiciones_vehiculo (
    id          SERIAL PRIMARY KEY,
    nombre      VARCHAR(50) UNIQUE NOT NULL,
    activo      BOOLEAN NOT NULL DEFAULT TRUE,
    created_at  TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS combustibles (
    id          SERIAL PRIMARY KEY,
    nombre      VARCHAR(50) UNIQUE NOT NULL,
    activo      BOOLEAN NOT NULL DEFAULT TRUE,
    created_at  TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS colores (
    id          SERIAL PRIMARY KEY,
    nombre      VARCHAR(50) UNIQUE NOT NULL,
    activo      BOOLEAN NOT NULL DEFAULT TRUE,
    created_at  TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS transmisiones (
    id          SERIAL PRIMARY KEY,
    nombre      VARCHAR(50) UNIQUE NOT NULL,
    activo      BOOLEAN NOT NULL DEFAULT TRUE,
    created_at  TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS departamentos (
    id          SERIAL PRIMARY KEY,
    nombre      VARCHAR(100) UNIQUE NOT NULL,
    activo      BOOLEAN NOT NULL DEFAULT TRUE,
    created_at  TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS municipios (
    id              SERIAL PRIMARY KEY,
    nombre          VARCHAR(100) NOT NULL,
    departamento_id INTEGER NOT NULL REFERENCES departamentos(id),
    activo          BOOLEAN NOT NULL DEFAULT TRUE,
    created_at      TIMESTAMP NOT NULL DEFAULT NOW(),
    UNIQUE (nombre, departamento_id)
);

-- ===============================
-- Clientes (propietarios externos)
-- ===============================

CREATE TABLE IF NOT EXISTS clientes (
    id          SERIAL PRIMARY KEY,
    nombre      VARCHAR(100) NOT NULL,
    apellidos   VARCHAR(150),
    contacto_1  VARCHAR(150) NOT NULL,
    contacto_2  VARCHAR(150),
    created_at  TIMESTAMP NOT NULL DEFAULT NOW()
);

-- ===============================
-- Vehiculos
-- ===============================

CREATE TABLE IF NOT EXISTS vehiculos (
    id                      BIGSERIAL PRIMARY KEY,
    vehiculo                VARCHAR(150) NOT NULL, -- Ej. "Mazda 3 Grand Touring 2020"
    categoria_id            INTEGER NOT NULL REFERENCES categorias_vehiculo(id),
    marca_id                INTEGER NOT NULL REFERENCES marcas_vehiculo(id),
    anio                    INTEGER NOT NULL CHECK (anio >= 1900),
    descripcion             VARCHAR(250),

    condicion_id            INTEGER NOT NULL REFERENCES condiciones_vehiculo(id),
    precio_base             INTEGER NOT NULL CHECK (precio_base >= 0),
    km                      INTEGER CHECK (km >= 0),
    cilindraje              INTEGER CHECK (cilindraje >= 0),
    combustible_id          INTEGER NOT NULL REFERENCES combustibles(id),
    color_id                INTEGER NOT NULL REFERENCES colores(id),
    transmision_id          INTEGER NOT NULL REFERENCES transmisiones(id),

    es_blindado             BOOLEAN NOT NULL DEFAULT FALSE,
    tiene_peritaje          BOOLEAN NOT NULL DEFAULT FALSE,

    ubi_departamento_id     INTEGER REFERENCES departamentos(id),
    ubi_municipio_id        INTEGER REFERENCES municipios(id),

    id_propietario          INTEGER REFERENCES clientes(id),   -- solo para origen = Captacion
    precio_sugerido_venta   INTEGER CHECK (precio_sugerido_venta >= 0),
    observaciones           TEXT,

    id_captador             INTEGER REFERENCES usuarios(id),   -- interno (vendedor)
    url                     TEXT,
    origen                  origen_vehiculo_enum NOT NULL,     -- 'Captacion' o 'Compra'

    fecha_ingreso           TIMESTAMP NOT NULL DEFAULT NOW(),
    estado                  estado_vehiculo_enum NOT NULL DEFAULT 'Activo',
    fecha_revision          DATE NOT NULL DEFAULT (NOW()::DATE + INTERVAL '15 days'),

    created_at              TIMESTAMP NOT NULL DEFAULT NOW()
);

-- Opcional: índice para catálogo (búsquedas rápidas)
CREATE INDEX IF NOT EXISTS idx_vehiculos_catalogo
    ON vehiculos (estado, origen, categoria_id, marca_id, anio);
