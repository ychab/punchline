from rest_framework.serializers import ModelSerializer

from .models import Author, Punchline, Reference


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class ReferenceSerializer(ModelSerializer):
    class Meta:
        model = Reference
        fields = '__all__'


class PunchlineSerializer(ModelSerializer):
    author = AuthorSerializer()
    reference = ReferenceSerializer()

    class Meta:
        model = Punchline
        fields = ('id', 'author', 'reference', 'text', 'created', 'modified')
