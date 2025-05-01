from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    idade = models.IntegerField()
    celular = models.CharField(max_length=20, default='00000000000')
    endereco = models.CharField(max_length=255)
    senha = models.CharField(max_length=128)  # Campo de senha adicionado
    
    def __str__(self):
        return self.nome
