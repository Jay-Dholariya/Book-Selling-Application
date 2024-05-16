# from django import forms 
from .models import Books2
from rest_framework import serializers

class booksSerializers(serializers.ModelSerializer):
    content = serializers.JSONField(required = False)
    title = serializers.CharField(max_length=25)
    
    class Meta :
        model = Books2
        fields = '__all__'
