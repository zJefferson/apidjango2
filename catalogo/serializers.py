from rest_framework import serializers

from .models import Filme, Avaliacao

class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email':{'write_only':True}
        }
        model = Avaliacao
        fields = (
            'id',
            'filme',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo'
        )


class FilmeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Filme
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo'
        )