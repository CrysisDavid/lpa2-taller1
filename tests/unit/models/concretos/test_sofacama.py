from src.models.concretos.sofacama import SofaCama


class TestSofaCama:
    def test_herencia_multiple(self):
        sofa_cama = SofaCama(
            "Sofa Cama Moderno",
            "Madera",
            "Blanco",
            500.0,
            3,
            tamaño_cama="Queen",
            incluye_colchon=False,
        )

        assert sofa_cama.capacidad_personas == 3

        assert sofa_cama.tamaño_cama == "Queen"

        assert hasattr(sofa_cama, "convertir_a_sofa")
        assert hasattr(sofa_cama, "convertir_a_cama")

    def test_resolucion_metodos(self):
        sofa_cama = SofaCama(
            "Sofa Cama", "Cuero", "Negro", 600.0, 2, tamaño_cama="queen"
        )
        precio = sofa_cama.calcular_precio()
        assert precio > 600.0
