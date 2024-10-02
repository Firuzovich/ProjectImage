from rest_framework import serializers
from .models import Worker, Region, District
from images.serializers import RegionSerializer, DistrictSerializer


class WorkerSerializer(serializers.ModelSerializer):
    district_id = serializers.IntegerField(write_only=True,required=False)
    region_id = serializers.IntegerField(write_only=True)  # Region ID maydoni
    region = RegionSerializer(read_only=True)  # Region ma'lumotlari
    district = DistrictSerializer(read_only=True)  # District ma'lumotlari

    class Meta:
        model = Worker
        fields = ['id', 'username', 'password', 'region_id', 'region', 'district_id','district']  # Kerakli maydonlarni ko'rsating