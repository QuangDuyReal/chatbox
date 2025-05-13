# Sử dụng image Python 3.9 làm base image
FROM python:3.9

# Cài đặt thư viện hệ thống (nếu cần thiết)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev

# Thiết lập thư mục làm việc trong container
WORKDIR /app

# Copy file requirements.txt vào container
COPY requirements.txt .

# Cài đặt tất cả dependencies từ requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ code vào container
COPY . .

# Mở cổng 8000 (cổng mặc định của FastAPI)
EXPOSE 8000

# Lệnh chạy khi container được khởi động
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
