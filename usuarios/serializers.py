from rest_framework import serializers
from .models import Usuario  # Importando o modelo de Usuario

class UsuarioSerializer(serializers.ModelSerializer):  # Usando ModelSerializer
    class Meta:
        model = Usuario  # Associando com o modelo Usuario
        fields = ['nome', 'email', 'senha', 'idade', 'celular', 'endereco']  # Definindo os campos do serializer
