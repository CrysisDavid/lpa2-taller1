import pytest

from src.models.concretos.cama import Cama


@pytest.mark.parametrize(
    ("tamaño", "extras", "precio_esperado"),
    [
        ("individual", 0, 500),
        ("matrimonial", 0, 700),
        ("queen", 300, 1200),
        ("king", 400, 1200),
    ],
)
def test_precio_de_cama(tamaño, extras, precio_esperado):
    cama = Cama("Cama", "Madera", "Blanco", 500, tamaño, incluye_colchon=extras == 300, tiene_cabecera=extras == 400)
    assert cama.calcular_precio() == precio_esperado


def test_cama_valida_tamaño_y_describe_caracteristicas():
    cama = Cama("Cama", "Madera", "Blanco", 500, incluye_colchon=True)
    with pytest.raises(ValueError):
        cama.tamaño = "doble"

    cama.tamaño = "queen"
    assert cama.calcular_precio() == 1200
    assert "Tamaño: queen" in cama.obtener_descripcion()
    assert "Incluye colchón: Sí" in cama.obtener_descripcion()
