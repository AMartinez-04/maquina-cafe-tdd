import unittest

from cafe import Azucarero, Cafetera, MaquinaCafe, Vaso


class MaquinaCafeTest(unittest.TestCase):
    def setUp(self):
        self.vaso_pequeno = Vaso("pequeno", cantidad=2, onzas=3)
        self.vaso_mediano = Vaso("mediano", cantidad=2, onzas=5)
        self.vaso_grande = Vaso("grande", cantidad=2, onzas=7)
        self.cafetera = Cafetera(onzas_cafe=20)
        self.azucarero = Azucarero(cucharadas=10)
        self.maquina = MaquinaCafe(
            self.cafetera,
            self.azucarero,
            [self.vaso_pequeno, self.vaso_mediano, self.vaso_grande],
        )

    def test_selecciona_vaso_pequeno_de_3_onzas(self):
        vaso = self.maquina.seleccionar_vaso("pequeno")

        self.assertEqual(3, vaso.onzas)

    def test_selecciona_vaso_mediano_de_5_onzas(self):
        vaso = self.maquina.seleccionar_vaso("mediano")

        self.assertEqual(5, vaso.onzas)

    def test_selecciona_vaso_grande_de_7_onzas(self):
        vaso = self.maquina.seleccionar_vaso("grande")

        self.assertEqual(7, vaso.onzas)

    def test_acepta_tipo_de_vaso_con_acentos_y_mayusculas(self):
        vaso = self.maquina.seleccionar_vaso("PEQUE\u00d1O")

        self.assertEqual(self.vaso_pequeno, vaso)

    def test_sirve_cafe_con_azucar_y_descuenta_insumos(self):
        mensaje = self.maquina.servir_cafe("mediano", cucharadas_azucar=2)

        self.assertEqual("Cafe servido", mensaje)
        self.assertEqual(1, self.vaso_mediano.cantidad)
        self.assertEqual(15, self.cafetera.onzas_cafe)
        self.assertEqual(8, self.azucarero.cucharadas)

    def test_muestra_mensaje_si_no_hay_vasos(self):
        maquina = MaquinaCafe(
            Cafetera(onzas_cafe=20),
            Azucarero(cucharadas=10),
            [Vaso("pequeno", cantidad=0, onzas=3)],
        )

        mensaje = maquina.servir_cafe("pequeno", cucharadas_azucar=1)

        self.assertEqual("No hay vasos", mensaje)

    def test_muestra_mensaje_si_no_hay_cafe(self):
        maquina = MaquinaCafe(
            Cafetera(onzas_cafe=2),
            Azucarero(cucharadas=10),
            [Vaso("pequeno", cantidad=1, onzas=3)],
        )

        mensaje = maquina.servir_cafe("pequeno", cucharadas_azucar=1)

        self.assertEqual("No hay cafe", mensaje)

    def test_muestra_mensaje_si_no_hay_azucar(self):
        maquina = MaquinaCafe(
            Cafetera(onzas_cafe=20),
            Azucarero(cucharadas=0),
            [Vaso("pequeno", cantidad=1, onzas=3)],
        )

        mensaje = maquina.servir_cafe("pequeno", cucharadas_azucar=1)

        self.assertEqual("No hay azucar", mensaje)

    def test_no_descuenta_insumos_cuando_no_puede_servir(self):
        maquina = MaquinaCafe(
            Cafetera(onzas_cafe=20),
            Azucarero(cucharadas=0),
            [Vaso("grande", cantidad=1, onzas=7)],
        )

        maquina.servir_cafe("grande", cucharadas_azucar=1)

        self.assertEqual(1, maquina.seleccionar_vaso("grande").cantidad)
        self.assertEqual(20, maquina.cafetera.onzas_cafe)

    def test_rechaza_cantidad_de_azucar_negativa(self):
        with self.assertRaises(ValueError):
            self.maquina.servir_cafe("pequeno", cucharadas_azucar=-1)


if __name__ == "__main__":
    unittest.main()
