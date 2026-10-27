import pytest

from src.models.mueble import Mueble


class TestMueble:
    def test_es_clase_abstracta(self):
        with pytest.raises(TypeError):
            mueble = Mueble("Mesa", "Madera", 100.0)

    def test_tiene_metodos_abstractos(self):
        assert hasattr(Mueble, "calcular_precio")
        assert hasattr(Mueble, "obtener_descripcion")

        assert Mueble.calcular_precio.__isabstractmethod__
        assert Mueble.obtener_descripcion.__isabstractmethod__
