import pytest
from services.tienda import TiendaMuebles

from src.models.composicion.comedor import Comedor
from src.models.concretos.mesa import Mesa
from src.models.concretos.silla import Silla


@pytest.fixture
def tienda():
    return TiendaMuebles("Mueblería de prueba")


@pytest.fixture
def silla():
    return Silla("Silla oficina", "Metal", "Negro", 100)


def test_tienda_agrega_muebles_y_comedores(tienda, silla):
    assert "agregado exitosamente" in tienda.agregar_mueble(silla)
    comedor = Comedor("Comedor", Mesa("Mesa", "Madera", "Natural", 300))
    assert "agregado exitosamente" in tienda.agregar_comedor(comedor)
    assert tienda.agregar_mueble(None) == "Error: El mueble no puede ser None"
    assert tienda.agregar_comedor(None) == "Error: El comedor no puede ser None"


def test_tienda_busca_y_filtra_muebles(tienda):
    sillas = [
        Silla("Silla oficina", "Metal", "Negro", 100),
        Silla("Silla comedor", "Madera", "Natural", 50),
    ]
    for mueble in sillas:
        tienda.agregar_mueble(mueble)

    assert tienda.buscar_muebles_por_nombre("  SILLA ") == sillas
    assert tienda.buscar_muebles_por_nombre("   ") == []
    assert tienda.filtrar_por_precio(sillas[0].calcular_precio(), sillas[0].calcular_precio()) == [sillas[0]]
    assert tienda.filtrar_por_precio(-10, 99) == [sillas[1]]
    assert tienda.filtrar_por_material(" madera ") == [sillas[1]]
    assert tienda.filtrar_por_material("") == []


def test_tienda_aplica_descuento_y_procesa_venta(tienda, silla):
    tienda.agregar_mueble(silla)
    assert "10%" in tienda.aplicar_descuento("sillas", 10)
    assert "entre 1 y 100" in tienda.aplicar_descuento("Silla", 0)

    venta = tienda.realizar_venta(silla, "Ana")
    assert venta["mueble"] == "Silla oficina"
    assert venta["cliente"] == "Ana"
    assert venta["descuento"] == 10
    assert venta["precio_final"] == pytest.approx(silla.calcular_precio() * 0.9)
    assert tienda.realizar_venta(silla)["error"] == ("El mueble no está disponible en inventario")


def test_tienda_estadisticas_y_reporte(tienda, silla):
    tienda.agregar_mueble(silla)
    tienda.aplicar_descuento("silla", 15)
    tienda.realizar_venta(silla, "Luis")

    estadisticas = tienda.obtener_estadisticas()
    assert estadisticas["total_muebles"] == 0
    assert estadisticas["ventas_realizadas"] == 1
    assert estadisticas["total_muebles_vendidos"] == 1
    assert estadisticas["valor_total_ventas"] == pytest.approx(93.5)
    assert estadisticas["descuentos_activos"] == {"Silla": 0.15}
    assert tienda.estadisticas() == estadisticas

    reporte = tienda.generar_reporte_inventario()
    assert "Mueblería de prueba" in reporte
    assert "Total de muebles: 0" in reporte
    assert "Silla: 15.0%" in reporte


def test_tienda_rechaza_mueble_con_precio_invalido(tienda):
    silla_sin_precio = Silla("Sin precio", "Metal", "Negro", 0)
    assert tienda.agregar_mueble(silla_sin_precio) == ("Error: El mueble debe tener un precio válido mayor a 0")


def test_tienda_propaga_errores_de_calculo_y_acceso_a_material(tienda):
    class MuebleConErrorDePrecio:
        def calcular_precio(self):
            raise RuntimeError("No se pudo calcular el precio")

    class MuebleConErrorDeMaterial:
        @property
        def material(self):
            raise RuntimeError("No se pudo obtener el material")

    tienda._inventario.append(MuebleConErrorDePrecio())
    with pytest.raises(RuntimeError, match="No se pudo calcular el precio"):
        tienda.filtrar_por_precio()
    with pytest.raises(RuntimeError, match="No se pudo calcular el precio"):
        tienda.obtener_estadisticas()

    tienda._inventario.clear()
    tienda._inventario.append(MuebleConErrorDeMaterial())
    with pytest.raises(RuntimeError, match="No se pudo obtener el material"):
        tienda.filtrar_por_material("madera")


def test_tienda_propaga_errores_al_calcular_valor_del_inventario(tienda):
    class MuebleConErrorDePrecio:
        def calcular_precio(self):
            raise RuntimeError("No se pudo calcular el precio")

    tienda._inventario.append(MuebleConErrorDePrecio())
    with pytest.raises(RuntimeError, match="No se pudo calcular el precio"):
        tienda.calcular_valor_inventario()
