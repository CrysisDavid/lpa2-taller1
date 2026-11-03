import pytest

from src.models.categorias.almacenamiento import Almacenamiento


class AlmacenamientoPrueba(Almacenamiento):
    def calcular_precio(self):
        return self.precio_base * self.calcular_factor_almacenamiento()

    def obtener_descripcion(self):
        return self.obtener_info_almacenamiento()


@pytest.fixture
def almacenamiento():
    return AlmacenamientoPrueba("Armario", "Madera", "Roble", 100, 4, 200)


def test_almacenamiento_es_abstracto():
    with pytest.raises(TypeError):
        Almacenamiento("Armario", "Madera", "Roble", 100, 4, 200)


def test_factor_y_descripcion_de_almacenamiento(almacenamiento):
    assert almacenamiento.calcular_factor_almacenamiento() == pytest.approx(1.19)  # nosec B101
    assert almacenamiento.obtener_info_almacenamiento() == (  # nosec B101
        "Compartimentos: 4, Capacidad: 200L"
    )
    assert almacenamiento.calcular_precio() == pytest.approx(119)  # nosec B101


@pytest.mark.parametrize(
    ("atributo", "valor"),
    [("num_compartimentos", 0), ("capacidad_litros", 0)],
)
def test_validacion_de_caracteristicas_de_almacenamiento(almacenamiento, atributo, valor):
    with pytest.raises(ValueError):
        setattr(almacenamiento, atributo, valor)
