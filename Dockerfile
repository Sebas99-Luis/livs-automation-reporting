FROM python:3.11-slim

# Instalar cron y dependencias del sistema
RUN apt-get update && apt-get install -y cron && apt-get clean

# Crear carpeta de trabajo
WORKDIR /app

# Copiar archivos del proyecto
COPY . /app

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements-prod.txt

# Copiar archivo de cron (lo crearemos luego)
COPY cronjob /etc/cron.d/pipeline-cron

# Dar permisos correctos al archivo de cron
RUN chmod 0644 /etc/cron.d/pipeline-cron

# Registrar el cronjob
RUN crontab /etc/cron.d/pipeline-cron

# Crear carpeta de logs dentro del contenedor
RUN mkdir -p /var/log/pipeline

# Comando por defecto: iniciar cron en primer plano
CMD ["cron", "-f"]