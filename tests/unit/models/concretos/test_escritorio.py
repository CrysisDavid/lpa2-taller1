from src.models.concretos.escritorio import Escritorio


def test_escritorio_calcula_precio_con_caracteristicas():
    escritorio = Escritorio("Escritorio", "Madera", "Negro", 400, "ovalado", True, 2, 1.8, True)

    assert escritorio.calcular_precio() == 570
    descripcion = escritorio.obtener_descripcion()
    assert "Forma=ovalado" in descripcion
    assert "Cajones=2" in descripcion
    assert "Iluminación=Sí" in descripcion


def test_escritorio_sin_extras():
    escritorio = Escritorio("Escritorio", "Metal", "Gris", 300)
    assert escritorio.calcular_precio() == 300
    assert "Cajones=0" in escritorio.obtener_descripcion()
