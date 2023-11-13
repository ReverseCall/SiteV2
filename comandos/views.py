from django.shortcuts import render
from .models import *
from datetime import datetime, time

def exibir_mensagem(request):
    agora = datetime.now().time()
    hoje = datetime.now().date()

    # Obtém a mensagem mais recente com tempo menor ou igual ao atual
    mensagem_recente = Mensagem.objects.filter(
        horario_envio__lte=agora,
        dia_envio=hoje
    ).order_by('-horario_envio').first()

    historico_mensagens = Mensagem.objects.exclude(
        dia_envio=hoje,
        horario_envio__gt=agora
    ).order_by('-dia_envio', '-horario_envio')

    return render(request, 'home.html', {'mensagem_recente': mensagem_recente, 'historico_mensagens': historico_mensagens})
