import pytest

from src.models.composicion.comedor import Comedor
from src.models.concretos.mesa import Mesa
from src.models.concretos.silla import Silla


@pytest.fixture
def comedor():
    mesa = Mesa(
        "Mesa familiar",
        "Roble",
        "Natural",
        200,
        largo=100,
        ancho=100,
        capacidad_personas=4,
    )
    sillas = [Silla(f"Silla {i}", "Roble", "Natural", 50) for i in range(4)]
    return Comedor("Familiar", mesa, sillas)


def test_comedor_compone_mesa_y_sillas(comedor):
    sillas = comedor.sillas
    assert comedor.nombre == "Familiar"
    assert comedor.mesa.nombre == "Mesa familiar"
    assert len(sillas) == 4
    sillas.clear()
    assert len(comedor.sillas) == 4
    assert len(comedor) == 5
    assert str(comedor) == "Comedor Familiar: Mesa + 4 sillas"


def test_comedor_agrega_y_quita_sillas(comedor):
    assert "Capacidad máxima: 4" in comedor.agregar_silla(Silla("Extra", "Roble", "Natural", 50))
    assert "removida" in comedor.quitar_silla(0)
    assert len(comedor) == 4
    assert comedor.quitar_silla(99) == "Índice de silla inválido"
    assert "removida" in comedor.quitar_silla()
    assert "removida" in comedor.quitar_silla()
    assert "removida" in comedor.quitar_silla()
    assert comedor.quitar_silla() == "No hay sillas para quitar"


def test_comedor_calcula_descuento_y_resumen(comedor):
    subtotal = comedor.mesa.calcular_precio() + sum(silla.calcular_precio() for silla in comedor.sillas)
    assert comedor.calcular_precio_total() == pytest.approx(subtotal * 0.95)

    resumen = comedor.obtener_resumen()
    assert resumen["total_muebles"] == 5
    assert resumen["capacidad_personas"] == 4
    assert resumen["precio_total"] == pytest.approx(subtotal * 0.95)
    assert set(resumen["materiales_utilizados"]) == {"Roble"}

    descripcion = comedor.obtener_descripcion_completa()
    assert "COMEDOR FAMILIAR" in descripcion
    assert "5% de descuento" in descripcion


def test_comedor_sin_sillas_y_capacidad_predeterminada():
    mesa = Mesa("Mesa pequeña", "Metal", "Negro", 100, capacidad_personas=2)
    comedor = Comedor("Pequeño", mesa)

    assert comedor.calcular_precio_total() == mesa.calcular_precio()
    assert "SILLAS: Ninguna incluida" in comedor.obtener_descripcion_completa()
    assert comedor._calcular_capacidad_maxima() == 2


def test_comedor_rechaza_tipo_incorrecto_si_ya_hay_sillas(comedor):
    assert comedor.agregar_silla("No es silla") == ("Error: Solo se pueden agregar objetos de tipo Silla")
