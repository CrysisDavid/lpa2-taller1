from src.models.concretos.sillon import Sillon


def test_sillon_precio_y_descripcion():
    sillon = Sillon(
        "Sillón reclinable",
        "Madera",
        "Azul",
        600,
        capacidad_personas=2,
        material_tapizado="Cuero",
        es_reclinable=True,
        tiene_reposapiés=True,
    )

    assert sillon.calcular_precio() == 1230
    descripcion = sillon.obtener_descripcion()
    assert "Capacidad=2 personas" in descripcion
    assert "Reclinable=Sí" in descripcion
    assert "Reposapiés=Sí" in descripcion


def test_sillon_sin_extras():
    sillon = Sillon("Sillón", "Madera", "Verde", 300, tiene_brazos=False)
    assert sillon.calcular_precio() == 300
    assert "Tapizado=N/A" in sillon.obtener_descripcion()
