import unittest
from src.estudiantes import registrar_estudiante, listar_estudiantes


class TestEstudiantes(unittest.TestCase):
    def setUp(self):
        self.estudiantes = []

    def test_registro_correcto(self):
        resultado = registrar_estudiante(
            self.estudiantes, "A001", "Ana Torres", "Computacion"
        )
        self.assertEqual(resultado["codigo"], "A001")
        self.assertEqual(len(self.estudiantes), 1)

    def test_rechaza_codigo_vacio(self):
        with self.assertRaises(ValueError):
            registrar_estudiante(self.estudiantes, "", "Ana Torres", "Computacion")

    def test_rechaza_nombre_vacio(self):
        with self.assertRaisesRegex(ValueError, "nombre"):
            registrar_estudiante(self.estudiantes, "A001", " ", "Computacion")

    def test_rechaza_programa_vacio(self):
        with self.assertRaisesRegex(ValueError, "programa"):
            registrar_estudiante(self.estudiantes, "A001", "Ana Torres", "")

    def test_rechaza_codigo_duplicado(self):
        registrar_estudiante(self.estudiantes, "A001", "Ana Torres", "Computacion")
        with self.assertRaisesRegex(ValueError, "Ya existe"):
            registrar_estudiante(self.estudiantes, "A001", "Luis Rojas", "Administracion")

    def test_lista_ordenada_por_codigo(self):
        registrar_estudiante(self.estudiantes, "A002", "Luis Rojas", "Administracion")
        registrar_estudiante(self.estudiantes, "A001", "Ana Torres", "Computacion")
        resultado = listar_estudiantes(self.estudiantes)
        self.assertEqual([e["codigo"] for e in resultado], ["A001", "A002"])

    def test_lista_vacia(self):
        resultado = listar_estudiantes(self.estudiantes)
        self.assertEqual(resultado, [])
        
if __name__ == "__main__":
    unittest.main()