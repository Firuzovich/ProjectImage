from django.urls import path, re_path
from images.views import SaveImagesInfoView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from foradmins.views import ManageAPIView, ManageImagesAPIView,CreateWorkerAPIView, ManageWorkersAPIView
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.contrib import admin



urlpatterns = [
    path('admin/',admin.site.urls), 
    path('api/_manage/', ManageAPIView.as_view(), name='manage_api'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/save-images-info/', SaveImagesInfoView.as_view(), name='save_images_info'),
    path('api/_manage/images/', ManageImagesAPIView.as_view(), name='manage_images'),
    path('api/_manage/user/create/', CreateWorkerAPIView.as_view(), name='create_worker'),
    path('api/_manage/user/', ManageWorkersAPIView.as_view(), name='manage_workers'),
    path('api/_manage/user/<int:pk>/', ManageWorkersAPIView.as_view(), name='manage_worker_detail'),  # PUT va DELETE uchun
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
        re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    ]

