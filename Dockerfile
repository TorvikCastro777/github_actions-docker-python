# Usamos una imagen ligera de Python
FROM python:3.9-slim

# Establecemos carpeta de trabajo
WORKDIR /app

# Copiamos archivos y dependencias
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

# Exponemos el puerto
EXPOSE 5000

# Comando para iniciar
CMD ["python", "app.py"]
