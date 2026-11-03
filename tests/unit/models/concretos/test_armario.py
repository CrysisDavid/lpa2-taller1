from src.models.concretos.armario import Armario


def test_armario_precio_y_descripcion_con_extras():
    armario = Armario(
        "Armario familiar",
        "Madera",
        "Blanco",
        500,
        num_puertas=3,
        num_cajones=2,
        tiene_espejos=True,
    )

    assert armario.calcular_precio() == 810
    descripcion = armario.obtener_descripcion()
    assert "Armario 'Armario familiar'" in descripcion
    assert "Puertas=3, Cajones=2, Espejos=Sí" in descripcion


def test_armario_convierte_precio_base_a_entero():
    armario = Armario("Armario", "Metal", "Negro", 100.9)
    assert armario.precio_base == 100
    assert armario.calcular_precio() == 200
