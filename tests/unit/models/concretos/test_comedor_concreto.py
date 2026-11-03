from src.models.concretos.comedor import Comedor
from src.models.concretos.mesa import Mesa
from src.models.concretos.silla import Silla


def test_comedor_agrega_quita_y_cuenta_sillas():
    comedor = Comedor(Mesa("Mesa", "Madera", "Natural", 300))
    silla = Silla("Silla", "Madera", "Natural", 50)

    comedor.agregar_silla(silla)
    comedor.agregar_silla(silla)
    assert comedor.cantidad_sillas() == 2
    assert comedor.calcular_precio_total() == (comedor.mesa.calcular_precio() + 2 * silla.calcular_precio())

    comedor.quitar_silla(silla)
    assert comedor.cantidad_sillas() == 1
    comedor.quitar_silla(Silla("Otra", "Metal", "Negro", 20))
    assert comedor.cantidad_sillas() == 1


def test_comedor_descripcion_incluye_componentes():
    mesa = Mesa("Mesa", "Madera", "Natural", 300)
    silla = Silla("Silla", "Metal", "Negro", 50)
    comedor = Comedor(mesa, [silla])

    descripcion = comedor.descripcion()
    assert "Mesa: Mesa" in descripcion
    assert "1. Silla: Silla" in descripcion
