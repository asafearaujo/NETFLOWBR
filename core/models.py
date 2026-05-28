from django.db import models
from django.utils import timezone
from datetime import timedelta
# Create your models here.

class Chamado(models.Model):
    STATUS_CHOICES = [
        ('aberto', 'Aberto'),
        ('progresso', 'Em Atendimento'),
        ('concluido', 'Finalizado'),
    ]

    # APENAS ESTA LINHA PARA PRIORIDADE (Sim ou Não)
    prioridade = models.BooleanField(default=False, verbose_name="É Prioridade?")
    
    cliente = models.CharField(max_length=100, default='Consumidor Final')
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='aberto')
    data_criacao = models.DateTimeField(auto_now_add=True)

    def esta_atrasado(self):
        # Se for prioridade, 2 dias. Se não, 3 dias.
        dias = 2 if self.prioridade else 3
        prazo_limite = timezone.now() - timedelta(days=dias)
        return self.status == 'aberto' and self.data_criacao < prazo_limite

    def __str__(self):
        return self.titulo