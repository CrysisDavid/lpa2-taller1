from io import StringIO
from unittest.mock import patch

from rich.console import Console

from services.tienda import TiendaMuebles
from src.models.composicion.comedor import Comedor
from src.models.concretos.mesa import Mesa
from src.models.concretos.silla import Silla
from ui.menu import MenuTienda


def crear_menu():
    tienda = TiendaMuebles("Mueblería de pruebas")
    tienda.agregar_mueble(Silla("Silla oficina", "Metal", "Negro", 100))
    salida = StringIO()
    menu = MenuTienda(tienda)
    menu.console = Console(file=salida, width=120)
    return menu, salida


def test_menu_muestra_inventario_y_maneja_catalogo_vacio():
    menu, salida = crear_menu()
    menu.mostrar_catalogo_completo()
    assert "Silla oficina" in salida.getvalue()

    menu.tienda._inventario.clear()
    menu.mostrar_catalogo_completo()
    assert "No hay muebles en el inventario" in salida.getvalue()


def test_menu_busca_y_filtra_interactivamente():
    menu, _ = crear_menu()
    with (
        patch("ui.menu.Prompt.ask", return_value="Silla"),
        patch("ui.menu.time.sleep"),
        patch.object(menu, "_mostrar_lista_muebles") as mostrar_lista,
    ):
        menu.buscar_muebles_interactivo()
    mostrar_lista.assert_called_once_with(menu.tienda._inventario)

    with (
        patch("ui.menu.IntPrompt.ask", side_effect=[0, 0]),
        patch("ui.menu.time.sleep"),
        patch.object(menu, "_mostrar_lista_muebles") as mostrar_lista,
    ):
        menu.filtrar_por_precio_interactivo()
    mostrar_lista.assert_called_once()

    with (
        patch("ui.menu.Prompt.ask", return_value="metal"),
        patch("ui.menu.time.sleep"),
        patch.object(menu, "_mostrar_lista_muebles") as mostrar_lista,
    ):
        menu.filtrar_por_material_interactivo()
    mostrar_lista.assert_called_once()


def test_menu_muestra_comedores_estadisticas_y_reporte():
    menu, salida = crear_menu()
    menu.mostrar_comedores()
    assert "No hay comedores disponibles" in salida.getvalue()
    comedor = Comedor("Comedor", Mesa("Mesa", "Madera", "Natural", 300))
    menu.tienda.agregar_comedor(comedor)
    menu.mostrar_comedores()
    assert "Comedor #1" in salida.getvalue()

    with patch("ui.menu.time.sleep"):
        menu.mostrar_estadisticas()
    assert "Estadísticas de la Tienda" in salida.getvalue()

    with (
        patch("ui.menu.time.sleep"),
        patch("ui.menu.Confirm.ask", return_value=False),
    ):
        menu.generar_reporte_interactivo()
    assert "REPORTE DE INVENTARIO" in salida.getvalue()


def test_menu_procesa_venta_y_aplicacion_de_descuento():
    menu, salida = crear_menu()
    with (
        patch("ui.menu.IntPrompt.ask", return_value=1),
        patch("ui.menu.Confirm.ask", return_value=True),
        patch("ui.menu.Prompt.ask", return_value="Eva"),
    ):
        menu.realizar_venta_interactiva()
    assert menu.tienda._inventario == []
    assert "Venta Exitosa" in salida.getvalue()

    with patch("ui.menu.IntPrompt.ask", side_effect=[1, 10]):
        menu.aplicar_descuentos_interactivo()
    assert menu.tienda._descuentos_activos == {"Silla": 0.1}


def test_menu_ejecuta_opcion_de_salida(monkeypatch):
    menu, _ = crear_menu()
    monkeypatch.setattr(menu, "mostrar_banner", lambda: None)
    monkeypatch.setattr(menu, "mostrar_menu_principal", lambda: 0)
    menu.ejecutar()
    assert menu.running is False


def test_menu_muestra_opcion_seleccionada(monkeypatch):
    menu, salida = crear_menu()
    monkeypatch.setattr("ui.menu.IntPrompt.ask", lambda *args, **kwargs: 7)
    assert menu.mostrar_menu_principal() == 7
    assert "MENÚ PRINCIPAL" in salida.getvalue()
