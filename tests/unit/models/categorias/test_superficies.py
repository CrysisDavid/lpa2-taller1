import pytest

from src.models.categorias.superficies import Superficie
from src.models.concretos.mesa import Mesa


@pytest.fixture
def mesa():
    return Mesa("Mesa", "Madera", "Natural", 200, largo=200, ancho=100, altura=75)


def test_superficie_es_abstracta():
    with pytest.raises(TypeError):
        Superficie("Mesa", "Madera", "Natural", 200, 200, 100, 75)


def test_calculo_de_area_y_factor(mesa):
    assert mesa.calcular_area() == 20_000
    assert mesa.calcular_factor_tamaño() == pytest.approx(1.1)
    assert mesa.obtener_info_superficie() == ("Dimensiones: 200x100x75cm (Área: 20000cm²)")


@pytest.mark.parametrize("atributo", ["largo", "ancho", "altura"])
def test_dimensiones_deben_ser_positivas(mesa, atributo):
    with pytest.raises(ValueError):
        setattr(mesa, atributo, 0)


def test_mesa_calcula_precio_y_descripcion(mesa):
    assert mesa.calcular_precio() == pytest.approx(220)
    assert "Mesa: Mesa" in mesa.obtener_descripcion()
    assert "Capacidad: 4 personas" in mesa.obtener_descripcion()


def test_mesa_valida_forma_y_capacidad(mesa):
    with pytest.raises(ValueError):
        mesa.forma = "triangular"
    with pytest.raises(ValueError):
        mesa.capacidad_personas = 0

    mesa.forma = "redonda"
    mesa.capacidad_personas = 8
    assert mesa.forma == "redonda"
    assert mesa.capacidad_personas == 8
    assert mesa.calcular_precio() == pytest.approx(370)
