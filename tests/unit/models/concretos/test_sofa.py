from src.models.concretos.sofa import Sofa


def test_sofa_calcula_precio_con_extras_y_describe():
    sofa = Sofa(
        "Sofá familiar",
        "Madera",
        "Gris",
        500,
        capacidad_personas=3,
        material_tapizado="tela",
        es_modular=True,
        incluye_cojines=True,
    )

    assert sofa.calcular_precio() == 1050
    descripcion = sofa.obtener_descripcion()
    assert "Capacidad: 3 personas" in descripcion
    assert "Modular: Sí" in descripcion
    assert "Incluye cojines: Sí" in descripcion


def test_sofa_sin_caracteristicas_adicionales():
    sofa = Sofa("Sofá", "Madera", "Negro", 500, 1, False, None, False, False, False)
    assert sofa.calcular_precio() == 500
