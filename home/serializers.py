from rest_framework import serializers
from .models import SinhVien, Lop

class SinhVienSerializer(serializers.ModelSerializer):
    class Meta:
        model = SinhVien
        fields = '__all__'

class LopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lop
        fields = '__all__'