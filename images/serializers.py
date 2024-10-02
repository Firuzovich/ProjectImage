from rest_framework import serializers
from .models import Images, Region, District

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'name']

class DistrictSerializer(serializers.ModelSerializer):
    region_id = serializers.IntegerField()

    class Meta:
        model = District
        fields = ['id', 'name', 'region_id']

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ['barcode', 'date', 'fish', 'region', 'district', 'post_name', 'photo']
    