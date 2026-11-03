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

        assert not silla_basica.tiene_ruedas
        assert not silla_basica.altura_regulable

    def test_calcular_precio(self, silla_basica):
        precio = silla_basica.calcular_precio()
        # calcular precio sin modificaciones
        print(precio)
        assert precio == 50.0

    def test_obtener_descripcion(self, silla_basica):
        descripcion = silla_basica.obtener_descripcion()
        assert "Silla Basica" in descripcion
        assert "Madera" in descripcion

    def test_regular_altura_y_silla_de_oficina(self):
        silla_oficina = Silla(
            "Silla oficina",
            "Metal",
            "Negro",
            100,
            altura_regulable=True,
            tiene_ruedas=True,
        )

        assert silla_oficina.regular_altura(75) == "Altura ajustada a 75 cm"
        assert silla_oficina.regular_altura(39) == ("La altura debe estar entre 40 y 100 cm")
        assert silla_oficina.es_silla_oficina() is True
        assert Silla("Silla fija", "Madera", "Natural", 50).es_silla_oficina() is False
