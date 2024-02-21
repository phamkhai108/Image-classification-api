from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Myapp.views import MyModelViewSet, ImageRecognitionAPIView

router = DefaultRouter()
router.register(r'api/mymodel', MyModelViewSet, basename='mymodel')

#đường dẫn các chức năng
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/image-recognition/', ImageRecognitionAPIView.as_view(), name='image-recognition'),
    path('api/mymodel/delete/<int:pk>/', MyModelViewSet.as_view({'delete': 'destroy'}), name='mymodel-delete')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
