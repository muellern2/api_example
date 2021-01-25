from rest_framework import serializers
from .models import language, paradigm, programmer

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = language
        fields = ('id', 'name', 'paradigm', 'url')

class ParadigmSerializer(serializers.ModelSerializer):
    class Meta:
        model = paradigm
        fields = ('id', 'name', 'url')

class ProgrammerSerializer(serializers.ModelSerializer):
    class Meta:
        model = programmer
        fields = ('id', 'name', 'url', 'languages')