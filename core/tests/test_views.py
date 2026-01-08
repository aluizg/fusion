from django.test import TestCase, Client
from django.urls import reverse_lazy

class IndexViewTests(TestCase):
    def setUp(self):
        self.form_data = {
            'nome': 'João Silva',
            'email': 'joaosilva@email.com',
            'assunto': 'Teste de assunto',
            'mensagem': 'Esta é uma mensagem de teste.',
        }
        self.cliente = Client()
        self.url = reverse_lazy('index')

    def test_form_valid(self):
        request = self.cliente.post(self.url, data=self.form_data)
        self.assertEqual(request.status_code, 302)  # Redireciona após sucesso
        messages = list(request.wsgi_request._messages)
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Mensagem enviada com sucesso!')

    def test_form_invalid(self):
        invalid_data = self.form_data.copy()
        invalid_data['email'] = 'emailinvalido'  # Email inválido
        request = self.cliente.post(self.url, data=invalid_data)
        self.assertEqual(request.status_code, 200)  # Permanece na página
        messages = list(request.wsgi_request._messages)
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Erro ao enviar mensagem. Verifique os dados preenchidos.')
