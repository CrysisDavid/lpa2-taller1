from src.models.concretos.cajonera import Cajonera


def test_cajonera_precio_y_descripcion_con_ruedas():
    cajonera = Cajonera("Cajonera", "Madera", "Natural", 200, num_cajones=4, tiene_ruedas=True)

    assert cajonera.calcular_precio() == 310
    descripcion = cajonera.obtener_descripcion()
    assert "Cajones=4" in descripcion
    assert "Ruedas=Sí" in descripcion


def test_cajonera_usa_opciones_por_defecto():
    cajonera = Cajonera("Cajonera", "Madera", "Natural", 100)
    assert cajonera.calcular_precio() == 160
    assert "Ruedas=No" in cajonera.obtener_descripcion()
