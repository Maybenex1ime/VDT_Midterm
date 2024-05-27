# Sử dụng image Python chính thức
FROM python:3.9-slim

# Đặt thư mục làm việc trong container
WORKDIR /app

# Sao chép file requirements.txt vào container
COPY requirements.txt .

# Cài đặt các thư viện cần thiết
RUN pip install --no-cache-dir -r requirements.txt

# Sao chép toàn bộ nội dung của thư mục hiện tại vào container
COPY . .

# Mở cổng 5000 để truy cập API
EXPOSE 5000

# Chạy ứng dụng API
CMD ["python", "app.py"]
