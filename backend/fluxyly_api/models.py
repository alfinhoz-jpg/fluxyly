from django.db import models
from django.contrib.auth.models import User

class Empresa(models.Model):
    nome = models.CharField(max_length=255)
    tipo = models.CharField(max_length=100)
    endereço = models.TextField()
    dono = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome
    
class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    localizacao = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.user.username
    
class Reserva(models.Model):
    STATUS_CHOICE = [
        ('pendente', 'Pendente')
        ('confirmado', 'Confirmado')
        ('cancelado', 'Cancelado')
    ]
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data = models.DateTimeField()
    horario = models.TimeField()
    participantes = models.TextField()
    
    def __str__(self):
        return f"{self.empresa.nome} - {self.data} às {self.horario} ({self.status})"