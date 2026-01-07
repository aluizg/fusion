from django import forms
from django.core.mail.message import EmailMessage

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='Email')
    assunto = forms.CharField(label='Assunto', max_length=150)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea)

    def enviar_email(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        dados = f'Contato de {nome} - {assunto}'
        corpo = f'Nome: {nome}\nEmail: {email}\n\nMensagem:\n{mensagem}'

        print(f'Enviando email:\nAssunto: {dados}\nCorpo:\n{corpo}')

        email_message = EmailMessage(
            subject=dados,
            body=corpo,
            from_email='hello@demomailtrap.co',
            to=['goncalves.aluiz@gmail.com'],
            headers={'Reply-To': email},
        )
        email_message.send()