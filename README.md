# Dự án phân loại động vật có vú qua API với 5 loài 'Cat', 'Dog', 'Rose', 'Elephant', 'Horse', 'Lion'
*chức năng :*
1. Dư đoán và trả về kết quả thông qua API.
   - Đầu vào: các trường, trong đó có trường hình ảnh
   - Đàu ra: kết quả dự đoán, gồm có tên đọngo vật và độ tin cậy mà mô hình dự đoán ra loài động vật đó.
2. Xem kết quả khi các giá trị đã up lên database
3. Xóa các đối tượng trong database thông qua id của chúng

*Tổng quan thực hiện project:*
1. Thu thập dữ liệu.
2. Train model phân loại 5 loài động vật với kiến trúc CNN dùng framework 'Tensorflow'. Chi tiết link (data và googlecolab): [Data and googlecolab](https://drive.google.com/drive/folders/1uoUC4oMCYdUQcrb2V5W-CXgbzeKRDh2S?usp=sharing)
3. Thực hiện xây dựng Api với Django-rest-framework.

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

## Hướng dẫn cách chạy project.
1. Tải về project bằng câu lệnh 'git clone https://github.com/phamkhai108/Image-classification-api.git'
2. Setup và cài đặt các thư viện cần thiết.
   - python version 3.11.6
   - Framework và thư viện: chạy lệnh 'pip install requirements.txt' để cài đặt các thư viện và framework cần thiết
3. Tiến hành chạy project.
   - Chuyển đến đường dẫn project chay câu lệnh 'py manage.py runserver 8100' ('8100' là cổng có thể thay đổi, nếu không có giá trị đó mặc định sẽ chạy trên cổng '8000')
   - khi chạy project chúng ta có các đường dẫn để thử như sau, mọi người có thể dùng postman để thử.
   - Gồm 3 đường dẫn:
     - Đường dẫn 'http://127.0.0.1:8000/api/mymodel/' với phương thức GET sẽ liệt kê các đối tượng có trong Database.
     - Đường dẫn 'http://127.0.0.1:8000/api/mymodel/' với phương thức POST sẽ đẩy các trường thông tin lên và nhận về là tên mô hình dự đoán cho bức ảnh (name) và độ tin cậy mà mô hình đưa ra cho 'name' (confidence)
     - Dể xóa dùng đường dẫn 'http://127.0.0.1:8000/api/mymodel/delete/20/' với phương thức DELETE để xóa đối tượng có id là 20 trong database. Có thể thay đổi giá trị '20' phù hợp với đối tượng cần xóa.
