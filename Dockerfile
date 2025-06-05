FROM python:3.11-slim

# ffmpeg (video işleme için)
RUN apt-get update && apt-get install -y ffmpeg

# Çalışma dizini
WORKDIR /app

# Tüm dosyaları kopyala
COPY . /app

# Gerekli Python kütüphanelerini yükle
RUN pip install --no-cache-dir -r requirements.txt

# Uygulamayı başlat
CMD ["python", "app.py"]
