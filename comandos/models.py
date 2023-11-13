from django.db import models

# Create your models here.

class Mensagem(models.Model):
    conteudo = models.TextField()
    dia_envio = models.DateField()
    horario_envio = models.TimeField()
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