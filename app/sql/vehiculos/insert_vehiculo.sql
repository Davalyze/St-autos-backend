INSERT INTO vehiculos (
    vehiculo,
    categoria_id,
    marca_id,
    anio,
    descripcion,

    condicion_id,
    precio_base,
    km,
    cilindraje,
    combustible_id,
    color_id,
    transmision_id,

    es_blindado,
    tiene_peritaje,

    ubi_departamento_id,
    ubi_municipio_id,

    id_propietario,
    precio_sugerido_venta,
    observaciones,

    url,
    origen
)
VALUES (
    %(vehiculo)s,
    %(categoria_id)s,
    %(marca_id)s,
    %(anio)s,
    %(descripcion)s,

    %(condicion_id)s,
    %(precio_base)s,
    %(km)s,
    %(cilindraje)s,
    %(combustible_id)s,
    %(color_id)s,
    %(transmision_id)s,

    %(es_blindado)s,
    %(tiene_peritaje)s,

    %(ubi_departamento_id)s,
    %(ubi_municipio_id)s,

    %(id_propietario)s,
    %(precio_sugerido_venta)s,
    %(observaciones)s,

    %(url)s,
    'Captacion'
)
RETURNING
    id,
    vehiculo,
    categoria_id,
    marca_id,
    anio,
    condicion_id,
    precio_base,
    km,
    cilindraje,
    combustible_id,
    color_id,
    transmision_id,
    es_blindado,
    tiene_peritaje,
    ubi_departamento_id,
    ubi_municipio_id,
    id_propietario,
    precio_sugerido_venta,
    observaciones,
    url,
    created_at;
