import pytest

from src.models.concretos.silla import Silla


class TestSilla:
    @pytest.fixture
    def silla_basica(self):
        return Silla(
            nombre="Silla Basica",
            material="Madera",
            color="negro",
            precio_base=50.0,
            material_tapizado="Madera",
            altura_regulable=False,
            tiene_ruedas=False,
            tiene_respaldo=False,
        )

    def test_instanciacion_correcta(self, silla_basica):
        assert silla_basica.nombre == "Silla Basica"
        assert silla_basica.material == "Madera"
        assert silla_basica.precio_base == 50.0

        assert silla_basica.tiene_ruedas == False
        assert silla_basica.altura_regulable == False

    def test_calcular_precio(self, silla_basica):
        precio = silla_basica.calcular_precio()
        # calcular precio sin modificaciones
        print(precio)
        assert precio == 50.0

    def test_obtener_descripcion(self, silla_basica):
        descripcion = silla_basica.obtener_descripcion()
        assert "Silla Basica" in descripcion
        assert "Madera" in descripcion
