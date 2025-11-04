from rest_framework import serializers
from django.db.models import Avg

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

    def validate_avaliacao(self, valor):
        if valor in range(1, 6):
            return valor
        raise serializers.ValidationError('A avaliação deve ser um inteiro entre 1 e 5')


class FilmeSerializer(serializers.ModelSerializer):

    media_avaliacoes = serializers.SerializerMethodField()

    class Meta:
        model = Filme
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes',
            'media_avaliacoes'
        )

    def get_media_avaliacoes(self, obj):
        media = obj.avaliacoes.aggregate(Avg('avaliacao')).get('avaliacao__avg')

        if media is None:
            return 0
        return round(media * 2) / 2