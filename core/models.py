import uuid
from django.db import models
from pictures.models import PictureField

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

def get_icon_name():
    map_icones = [
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Grafico'),
        ('lni-users', 'Usuarios'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
        ('lni-laptop-phone', 'Laptop e Celular'),
        ('lni-leaf', 'Folha'),
        ('lni-layers', 'Camadas'),
        ('lni-lamp', 'Lâmpada'),
        ('lni-target', 'Alvo')
    ]
    return map_icones

class Base(models.Model):
    criacao = models.DateField('Data de Criação', auto_now_add=True)
    modificacao = models.DateField('Data de Modificação', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

class Servico(Base):
    nome = models.CharField('Nome', max_length=100)
    descricao = models.TextField('Descrição', blank=True)
    icone = models.CharField('Ícone', max_length=20, choices=get_icon_name)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.nome

class Cargo(Base):
    nome = models.CharField('Nome', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.nome


class Equipe(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey(Cargo, verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.TextField('Biografia', blank=True)
    facebook = models.URLField('Facebook', blank=True)
    instagram = models.URLField('Instagram', blank=True)
    twitter = models.URLField('Twitter', blank=True)

    foto_width = models.PositiveIntegerField(editable=False, null=True)
    foto_height = models.PositiveIntegerField(editable=False, null=True)

    foto = PictureField('Foto',
                        upload_to=get_file_path,
                        aspect_ratios=[None, "1/1", "16/9"],     # Define proporções permitidas
                        container_width=480,                     # Define largura máxima do layout
                        width_field = 'foto_width',
                        height_field = 'foto_height'
                        )
    class Meta:
        verbose_name = 'Equipe'
        verbose_name_plural = 'Membros da Equipe'

    def __str__(self):
        return self.nome

class Recurso(Base):
    titulo = models.CharField('Título', max_length=100)
    descricao = models.TextField('Descrição', blank=True)
    icone = models.CharField('Ícone', max_length=20, choices=get_icon_name)

    class Meta:
        verbose_name = 'Recurso'
        verbose_name_plural = 'Recursos'

    def __str__(self):
        return self.titulo