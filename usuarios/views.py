from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UsuarioSerializer
from .models import Usuario

@api_view(['POST'])
def cadastrar_usuario(request):
     if request.method == 'POST':
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'usuario': serializer.data}, status=201)
        else:
            print(serializer.errors)  # <-- Isso vai mostrar no terminal os erros
            return Response(serializer.errors, status=400)

@api_view(['GET'])
def listar_usuarios(request):
    if request.method == 'GET':
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)
