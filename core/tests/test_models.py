import uuid
from django.test import TestCase
from model_mommy import mommy
from core.models import get_file_path

class GetFilePathTests(TestCase):
    def setUp(self):
        self.filename_uuid = f'{uuid.uuid4()}.png'
        self.filename = '"test_image.png"'

    def test_get_file_path(self):
        arquivo = get_file_path(None, self.filename)
        self.assertTrue(len(self.filename_uuid), len(arquivo))

class ServicoTests(TestCase):
    def setUp(self):
        self.servico = mommy.make('Servico')

    def test_str(self):
        self.assertEqual(str(self.servico), self.servico.nome)

class CargoTests(TestCase):
    def setUp(self):
        self.cargo = mommy.make('Cargo')

    def test_str(self):
        self.assertEqual(str(self.cargo), self.cargo.nome)

class EquipeTests(TestCase):
    def setUp(self):
        self.equipe = mommy.make('Equipe')

    def test_str(self):
        self.assertEqual(str(self.equipe), self.equipe.nome)

class RecursosTests(TestCase):
    def setUp(self):
        self.recurso = mommy.make('Recurso')

    def test_str(self):
        self.assertEqual(str(self.recurso), self.recurso.titulo)