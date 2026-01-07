#class based view
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Servico, Equipe, Recurso
from .forms import ContatoForm

class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def form_valid(self, form, *args, **kwargs):
        # Envia o email
        form.enviar_email()
        messages.success(self.request, 'Mensagem enviada com sucesso!')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        print(f'Formulário inválido: {form.errors}')
        messages.error(self.request, 'Erro ao enviar mensagem. Verifique os dados preenchidos.')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)

    def get_context_data(self, **kwargs):
        # Recupera o contexto da pagina
        context = super().get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all()
        context['equipes'] = Equipe.objects.all()
        context['recursos'] = Recurso.objects.all()
        return context