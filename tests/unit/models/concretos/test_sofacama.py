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
        sofa_cama = SofaCama("Sofa Cama", "Cuero", "Negro", 600.0, 2, tamaño_cama="queen")
        precio = sofa_cama.calcular_precio()

        assert precio > 600.0

    def test_conversion_entre_modos_y_capacidad(self):
        sofa_cama = SofaCama(
            "Convertible",
            "Madera",
            "Gris",
            500,
            capacidad_personas=3,
            tamaño_cama="queen",
            mecanismo_conversion="hidraulico",
        )

        assert sofa_cama.modo_actual == "sofa"
        assert sofa_cama.convertir_a_sofa() == "El sofá-cama ya está en modo sofá"
        assert "convertido a cama" in sofa_cama.convertir_a_cama()
        assert sofa_cama.convertir_a_cama() == "El sofá-cama ya está en modo cama"
        assert sofa_cama.convertir_a_sofa().startswith("Cama convertida a sofá")
        assert sofa_cama.obtener_capacidad_total() == {
            "como_sofa": 3,
            "como_cama": 2,
        }
        assert str(sofa_cama) == "Sofá-cama Convertible (modo: sofa)"
        assert "Tamaño como cama: queen" in sofa_cama.obtener_descripcion()

    def test_precio_incluye_tamaño_colchon_y_mecanismo(self):
        sofa_cama = SofaCama(
            "Convertible",
            "Madera",
            "Gris",
            500,
            capacidad_personas=1,
            material_tapizado=None,
            tamaño_cama="king",
            incluye_colchon=True,
            mecanismo_conversion="electrico",
        )

        assert sofa_cama.calcular_precio() == 1950
