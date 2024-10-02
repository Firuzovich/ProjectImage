from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAdminUser
from images.models import Images
from images.serializers import ImageSerializer
from .models import Worker
from .serializers import WorkerSerializer

class ManageAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                return Response({"message": "Successfully logged in"}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        except User.DoesNotExist:
            return Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)

class ManageImagesAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        images = Images.objects.all()  # Barcha rasmlar
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class CreateWorkerAPIView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        serializer = WorkerSerializer(data=request.data)
        if serializer.is_valid():
            region_id = serializer.validated_data.pop('region_id')
            district_id = serializer.validated_data.pop('district_id', None)  # None bo'lsa, null oladi
            serializer.save(region_id=region_id, district_id=district_id)  # Saqlash
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ManageWorkersAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        workers = Worker.objects.all()
        serializer = WorkerSerializer(workers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
class ManageWorkersAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        workers = Worker.objects.all()
        serializer = WorkerSerializer(workers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        try:
            worker = Worker.objects.get(pk=pk)
        except Worker.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = WorkerSerializer(worker, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            worker = Worker.objects.get(pk=pk)
            worker.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Worker.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)