# Dự án phân loại hoa qua API với 5 loài hoa 'Tulip', 'Sunflower', 'Rose', 'Dandelion', 'Daisy'
*chức năng :*
1. Dư đoán và trả về kết quả thông qua API.
   - Đầu vào: các trường, trong đó có trường hình ảnh
   - Đàu ra: kết quả dự đoán, gồm có tên loài hoa và độ tin cậy mà mô hình dự đoán ra loài hoa đó.
2. Xem kết quả khi các giá trị đã up lên database
3. Xóa các đối tượng trong database thông qua id của chúng
## công nghệ sử dụng
1. Ngôn ngữ lập trình:  python
2. Framework và thư viện chính: Django, tensorflow, Pillow, numpy
   - Django: tạo khung viết api.
     > Link document: [Django-rest-framewor](https://www.django-rest-framework.org/)
   - tensorflow: tạo dựng và train model.
     > Link tìm hiểu và học tập: [Tensorflow](https://www.tensorflow.org/?hl=vi)
   - Pillow: dùng để lấy ảnh đầu vào từ request
     > Link tham khảo: [Pillow](https://pypi.org/project/pillow/)
   - numpy: xử lý ảnh và chuyển ảnh về mảng phù hợp với việc dùng model dự đoán và đưa ra kết quả
     > Link tham khảo: [Numpy](https://numpy.org/)
## Một số hình ảnh dùng postman để thử với API đã viết để xem kết quả
1. Thử xem kết quả nhận diện khi post lên các giá trị và hình ảnh
   - giá trị trả về 'name' là tên hoa dự đoán được khi post lên.
   - giá trị 'confidence' là độ tin cậy mà mô hình dự đoán cho kết quả 'name'
   - 
![Hoa Daisy](https://drive.google.com/file/d/1mSSSrzVDU-PC1IEeWfkRQHEpMNvDwIbP/view?usp=sharing)
![Hoa Tulip](https://drive.google.com/file/d/1r3zIVZaBkOVG4b86BtvaVbMNIIlD9xkc/view?usp=sharing)
![Hoa Rose](https://drive.google.com/file/d/1pjdm0inSb-ytvZk0F-SbIFNQI8rgkG9z/view?usp=sharing)
![Hoa Dandelion](https://drive.google.com/file/d/1CPHgdK76MuC0QVRzz_96Gq0iQBZ9Lwxw/view?usp=sharing)
![Hoa Sunflower](https://drive.google.com/file/d/1W7Tk-4dxPMQekHWBgmmHPqF1P5I06tTf/view?usp=sharing)
2. video demo 
