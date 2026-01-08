from django.test import testcases
from core.forms import ContatoForm

class ContatoFormTestCase(testcases.TestCase):
    def setUp(self):
        self.form_data = {
            'nome': 'João Silva',
            'email': 'joaosilva@email.com',
            'assunto': 'Teste de assunto',
            'mensagem': 'Esta é uma mensagem de teste.',
        }
        self.form = ContatoForm(data=self.form_data)

    def test_enviar_email(self):
        form1 = ContatoForm(data=self.form_data)
        form1.is_valid()
        result1 = form1.enviar_email()

        form2 = self.form
        form2.is_valid()
        result2 = form2.enviar_email()

        self.assertEqual(result1, result2)
