from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import FilmeAPIView, AvaliacaoAPIView, FilmesAPIView, AvaliacoesAPIView, FilmeViewSet, AvaliacaoViewSet


router = SimpleRouter()
router.register('filmes', FilmeViewSet)
router.register('avaliacoes', AvaliacaoViewSet)



urlpatterns = [
    path('filmes/', FilmesAPIView.as_view(), name ='filmes'),
    path('filmes/<int:pk>', FilmeAPIView.as_view(), name='filme'),

    path('filmes/<int:filme_pk>/avaliacoes/', AvaliacoesAPIView.as_view(),name='filmes_avaliacoes'),
    path('filmes/<int:filme_pk>/avaliacoes/<int:avaliacao_pk>/', AvaliacaoAPIView.as_view(),name='filme_avaliacao'),

    path('avaliacoes/', AvaliacoesAPIView.as_view(), name ='avaliacoes'),
    path('avaliacoes/<int:avaliacao_pk>', AvaliacaoAPIView.as_view(), name='avaliacao')
]