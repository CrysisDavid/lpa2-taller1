import pytest

from src.models.concretos.silla import Silla
from src.models.mueble import Mueble


class TestMueble:
    def test_es_clase_abstracta(self):
        with pytest.raises(TypeError):
            Mueble("Mesa", "Madera", 100.0)

    def test_tiene_metodos_abstractos(self):
        assert hasattr(Mueble, "calcular_precio")
        assert hasattr(Mueble, "obtener_descripcion")

        assert Mueble.calcular_precio.__isabstractmethod__
        assert Mueble.obtener_descripcion.__isabstractmethod__

    def test_propiedades_y_representaciones(self):
        silla = Silla("Silla", "Madera", "Negro", 50)
        silla.nombre = "  Silla nueva  "
        silla.material = "  Roble  "
        silla.color = "  Blanco  "
        silla.precio_base = 75

        assert silla.nombre == "Silla nueva"
        assert silla.material == "Roble"
        assert silla.color == "Blanco"
        assert silla.precio_base == 75
        assert str(silla) == "Silla nueva de Roble en color Blanco"
        assert repr(silla) == ("Mueble(nombre='Silla nueva', material='Roble', color='Blanco', " "precio_base=75)")

    @pytest.mark.parametrize(
        ("atributo", "valor"),
        [
            ("nombre", ""),
            ("material", "  "),
            ("color", ""),
            ("precio_base", -1),
        ],
    )
    def test_propiedades_validan_valores(self, atributo, valor):
        silla = Silla("Silla", "Madera", "Negro", 50)
        with pytest.raises(ValueError):
            setattr(silla, atributo, valor)
