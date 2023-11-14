from django.db import models
from datetime import timedelta
from datetime import datetime, time, timezone

# Create your models here.

class Mensagem(models.Model):
    TIPO_CHOICE = [
        ('dica', 'Dica'),
        ('informacao', 'Informação'),
    ]

    conteudo = models.TextField()
    dia_envio = models.DateField()
    horario_envio = models.TimeField()
    tipo_mensagem = models.CharField(max_length=20, choices=TIPO_CHOICE, default='informacao')
    ultima = models.BooleanField(default=False)
    mensagem_adicional = models.TextField(blank=True, null=True)
    audio_url = models.FileField(upload_to='audios/', null=True, blank=True)


    def __str__(self):
        return self.conteudo
    
class Imagem(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    imagem = models.ImageField(upload_to='imagens/')
    
    def __str__(self):
        return self.nome