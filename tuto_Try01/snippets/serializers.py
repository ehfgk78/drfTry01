from rest_framework import serializers
from .models import LANGUAGE_CHOICES, STYLE_CHOICES, Snippet


class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Snippet
        fields = (
            'id',
            'owner',
            'title',
            'code',
            'linenos',
            'language',
            'style',
        )
