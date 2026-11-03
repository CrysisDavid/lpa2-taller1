import pytest

from src.models.concretos.silla import Silla


@pytest.fixture
def silla():
    return Silla(
        "Silla ergonómica",
        "Metal",
        "Negro",
        100,
        tiene_respaldo=True,
        material_tapizado="Cuero",
        altura_regulable=True,
        tiene_ruedas=True,
    )


def test_asiento_calcula_comodidad_y_obtiene_informacion(silla):
    assert silla.calcular_factor_comodidad() == pytest.approx(1.3)
    assert silla.obtener_info_asiento() == ("Capacidad: 1 personas, Respaldo: Sí, Tapizado: Cuero")
    assert silla.calcular_precio() == 180


def test_asiento_valida_capacidad_y_permite_actualizar_atributos(silla):
    with pytest.raises(ValueError):
        silla.capacidad_personas = 0

    silla.capacidad_personas = 2
    silla.tiene_respaldo = False
    silla.material_tapizado = "Tela"
    assert silla.capacidad_personas == 2
    assert silla.calcular_factor_comodidad() == pytest.approx(1.15)


def test_asiento_sin_tapizado():
    silla = Silla("Taburete", "Madera", "Natural", 75, tiene_respaldo=False)
    assert silla.obtener_info_asiento() == "Capacidad: 1 personas, Respaldo: No"
    assert silla.calcular_factor_comodidad() == 1
