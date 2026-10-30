import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'estudiantes'))
from app import app


class TestEstudiantesAPI(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.cliente = app.test_client()

    def test_get_estudiantes(self):
        respuesta = self.cliente.get('/estudiantes')
        self.assertEqual(respuesta.status_code, 200)
        self.assertEqual(respuesta.get_json(), {
            'mensaje': 'Lista de estudiantes obtenida correctamente.',
            'estudiantes': ['Ana', 'Carlos', 'María'],
        })

    def test_post_estudiante(self):
        respuesta = self.cliente.post('/estudiantes', json={'nombre': 'Pedro'})
        self.assertEqual(respuesta.status_code, 200)
        self.assertEqual(respuesta.get_json(), {
            'mensaje': 'Estudiante agregado correctamente.',
            'estudiante': 'Pedro',
        })

    def test_put_estudiante(self):
        respuesta = self.cliente.put('/estudiantes/1', json={'nombre': 'Pedro Ramírez'})
        self.assertEqual(respuesta.status_code, 200)
        self.assertEqual(respuesta.get_json(), {
            'mensaje': 'Estudiante actualizado correctamente.',
            'id': 1,
        })

    def test_delete_estudiante(self):
        respuesta = self.cliente.delete('/estudiantes/1')
        self.assertEqual(respuesta.status_code, 200)
        self.assertEqual(respuesta.get_json(), {
            'mensaje': 'Estudiante eliminado correctamente.',
            'id': 1,
        })

    def test_post_sin_nombre(self):
        respuesta = self.cliente.post('/estudiantes', json={})
        self.assertEqual(respuesta.status_code, 400)

    def test_put_sin_nombre(self):
        respuesta = self.cliente.put('/estudiantes/1', json={})
        self.assertEqual(respuesta.status_code, 400)


if __name__ == '__main__':
    unittest.main()
