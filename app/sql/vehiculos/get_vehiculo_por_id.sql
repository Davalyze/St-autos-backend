SELECT
    v.id,
    v.vehiculo,
    v.anio,
    v.precio_base,
    v.precio_sugerido_venta,
    v.km,
    v.cilindraje,
    v.descripcion,
    v.origen,

    m.nombre AS marca,
    c.nombre AS categoria,
    co.nombre AS color,
    cb.nombre AS combustible,
    t.nombre AS transmision,
    con.nombre AS condicion,

    d.nombre AS departamento,
    mu.nombre AS municipio,

    cli.nombre_completo AS propietario,
    cli.contacto_1 AS contacto_propietario,

    v.es_blindado,
    v.tiene_peritaje,
    v.observaciones,
    v.url,

    img.blob_name

FROM vehiculos v
LEFT JOIN marcas_vehiculo m ON m.id = v.marca_id
LEFT JOIN categorias_vehiculo c ON c.id = v.categoria_id
LEFT JOIN colores co ON co.id = v.color_id
LEFT JOIN combustibles cb ON cb.id = v.combustible_id
LEFT JOIN transmisiones t ON t.id = v.transmision_id
LEFT JOIN condiciones_vehiculo con ON con.id = v.condicion_id
LEFT JOIN departamentos d ON d.id = v.ubi_departamento_id
LEFT JOIN municipios mu ON mu.id = v.ubi_municipio_id
LEFT JOIN clientes cli ON cli.id = v.id_propietario
left join producto_imagenes as img on img.vehiculo_id = v.id
WHERE v.id = %(id)s;
