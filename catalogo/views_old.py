from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Filme, Avaliacao
from .serializers import FilmeSerializer, AvaliacaoSerializer


class FilmeAPIView(APIView):
    """
    API de avaliação de filmes
    """
    def get(self, request):
        print(request)
        filmes = Filme.objects.all()
        serializer = FilmeSerializer(filmes, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = FilmeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class AvaliacaoAPIView(APIView):
    """
    API de avaliação de filmes
    """
    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = AvaliacaoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)