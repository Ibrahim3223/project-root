FROM python:3.11-slim

# Sistem bağımlılıklarını yükle
RUN apt-get update && apt-get install -y ffmpeg

# Proje dosyalarını ekle
WORKDIR /app
COPY . /app

# Python bağımlılıklarını yükle
RUN pip install --no-cache-dir -r requirements.txt

# Uygulamayı başlat
CMD ["python", "app.py"]
