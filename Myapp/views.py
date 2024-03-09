from rest_framework import viewsets, status
from rest_framework.parsers import MultiPartParser, FormParser
from .models import MyModel
from .serializers import MyModelSerializer
import os
from rest_framework.views import APIView
from rest_framework.response import Response
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model
from django.conf import settings


class MyModelViewSet(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        serializer.save(image=self.request.data.get('image'))

    def perform_destroy(self, instance):
        if instance.image:
            instance.image.delete()
        instance.delete()


class ImageRecognitionAPIView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            # Lấy đường dẫn đến mô hình nhận diện hình ảnh
            model_path = os.path.join(settings.BASE_DIR, 'Train/animal_classifier_cnn.h5')

            # Load mô hình
            model = load_model(model_path)

            # Lấy hình ảnh từ request
            image = Image.open(request.data['image'])
            image = image.resize((150, 150))

            # Chuyển đổi hình ảnh thành mảng numpy và mở rộng thêm một chiều
            image_array = np.array(image) / 255.0
            image_array = np.expand_dims(image_array, axis=0)

            # Dự đoán
            predictions = model.predict(image_array)

            # Danh sách các nhãn
            labels = ['Cat', 'Dog', 'Elephant', 'Horse', 'Lion']


            # Lấy kết quả
            result = {
                'class_name': labels[np.argmax(predictions[0])],
                'confidence': float(np.max(predictions[0]))
            }

            return Response(result, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def delete(self, request, *args, **kwargs):
        try:
            # Lấy ID của đối tượng cần xóa từ tham số URL
            image_id = kwargs.get('pk')
            
            # Xác định đối tượng cần xóa từ cơ sở dữ liệu
            instance = MyModel.objects.get(pk=image_id)

            # Xóa hình ảnh từ thư mục media
            image_path = instance.image.path
            if os.path.exists(image_path):
                os.remove(image_path)

            # Xóa đối tượng khỏi cơ sở dữ liệu
            instance.delete()

            return Response({'message': 'Resource deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except MyModel.DoesNotExist:
            return Response({'error': 'Resource not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
