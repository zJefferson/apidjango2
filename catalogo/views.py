from django.shortcuts import get_object_or_404
from rest_framework import generics

from rest_framework import viewsets

from .models import Filme, Avaliacao
from .serializers import FilmeSerializer, AvaliacaoSerializer

from rest_framework import permissions

from .permissions import EhSuperUser


"""
API V1
"""

class FilmesAPIView(generics.ListCreateAPIView):
    
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer


class FilmeAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer


class AvaliacoesAPIView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_queryset(self):
        if self.kwargs.get('filme_pk'):
            return self.queryset.filter(filme_id=self.kwargs.get('filme_pk'))
        return self.queryset.all()


class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_object(self):
        if self.kwargs.get('filme_pk'):
            return get_object_or_404(self.get_queryset(),filme_id=self.kwargs.get('filme_pk'),pk=self.kwargs.get('avaliacao_pk'))
        return get_object_or_404(self.get_queryset(),pk=self.kwargs.get('avaliacao_pk'))
    

"""
API V2
"""

class FilmeViewSet(viewsets.ModelViewSet):
    permission_classes = (
        EhSuperUser, #se essa classe resolve a permissão, não passa para a próxima
        permissions.DjangoModelPermissions, 
    )
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer


class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer