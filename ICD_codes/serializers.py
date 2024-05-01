from rest_framework import serializers
from .models import MainCode, SubCode

class MainCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainCode
        fields = ['ICD_main_code', 'description']

class SubCodeSerializer(serializers.ModelSerializer):
    # Nested serialization to display details from the MainCode model
    ICD_main_code = MainCodeSerializer(read_only=True)
    class Meta:
        model = SubCode
        fields = ['ICD_sub_code', 'ICD_main_code', 'description']

    def __str__(self):
        return self.ICD_sub_code
