from django.db import models


class Evento(models.Model):
    nome_evento = models.CharField(max_length=100)
    descricao_evento = models.TextField()
    imagem_evento = models.ImageField(upload_to='eventos/')
    preco_ingresso = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_ingresso = models.PositiveIntegerField()
    data_criacao_evento = models.DateTimeField(auto_now_add=True)
    data_evento = models.DateField()  # Data específica do evento
    hora_evento = models.TimeField()  # Horário específico do evento

    def __str__(self):
        return self.nome_evento
