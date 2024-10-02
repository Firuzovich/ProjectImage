from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from .models import Images, Region, District
from .serializers import ImageSerializer

class SaveImagesInfoView(APIView):
    def post(self, request):
        # Tokenni tekshirish
        token = request.headers.get('Authorization')
        if token != settings.AUTH_TOKEN:
            return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)

        # Region va Districtni tekshirish va qo'shish
        region_name = request.data.get('region')
        district_name = request.data.get('district')

        region, _ = Region.objects.get_or_create(name=region_name)
        district, _ = District.objects.get_or_create(name=district_name, region=region)

        # Ma'lumotlarni saqlash
        data = request.data
        data['region'] = region.id
        data['district'] = district.id

        serializer = ImageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
