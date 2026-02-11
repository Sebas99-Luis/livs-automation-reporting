# 📦 LIVS Automation Pipeline

Automatización diaria para ingestión, validación, limpieza y carga de datos en PostgreSQL usando Docker y cron.

---

## 🧭 Descripción general

Este proyecto implementa un pipeline totalmente automatizado que procesa archivos CSV diarios provenientes del sistema de ventas de LIVS. El flujo incluye:

- Ingesta automática de archivos  
- Validación y limpieza  
- Manejo de errores  
- Carga en PostgreSQL  
- Logging persistente  
- Ejecución diaria mediante cron dentro de Docker  

El objetivo es entregar un sistema estable, reproducible y fácil de mantener, sin depender de instalaciones locales de Python.

---


## 🔄 Flujo del pipeline

<img width="1024" height="1024" alt="image" src="https://github.com/user-attachments/assets/232bd253-1ea6-4747-9520-f31aa5deab91" />



---

## ⚙️ Funcionamiento del pipeline

### 1. Ingesta  
Los archivos CSV se colocan en `data/incoming/`.

### 2. Validación  
Se revisan columnas obligatorias, tipos de datos y estructura.

### 3. Limpieza  
Correcciones de formato, normalización, manejo de nulos, estandarización de categorías.

### 4. Manejo de errores  
Si un archivo falla validación o limpieza:

- Se mueve a `data/bad/`  
- Se registra el error en `logs/pipeline.log`

### 5. Carga en PostgreSQL  
Los datos limpios se insertan en la tabla


### 6. Logging  
Cada ejecución escribe:

- Fecha y hora  
- Archivo procesado  
- Registros insertados  
- Errores encontrados  

---


### 6. Logging  
Cada ejecución escribe:

- Fecha y hora  
- Archivo procesado  
- Registros insertados  
- Errores encontrados  

---

## 🐳 Ejecución con Docker

### Construir imágenes
docker-compose build --no-cache

### Levantar servicios
docker-compose up -d

Esto inicia:

- `livs_db` → PostgreSQL  
- `livs_pipeline` → pipeline + cron  

---

## ⏰ Automatización con cron

El contenedor ejecuta el pipeline todos los días a las **06:00**.

Contenido del archivo `pipeline-cron`:
docker exec -it livs_pipeline sh -c "python /app/run_pipeline.py"


Revisar log:
tail -n 50 logs/pipeline.log


---

## 🗄️ Acceso a PostgreSQL

Conexión local:

- Host: `localhost`  
- Puerto: `5432`  
- Usuario: definido en `.env`  
- Base de datos: `livs`  

Ejemplo:
psql -h localhost -U postgres -d livs


---

## 📌 Estado final del proyecto

Este proyecto entrega:

- Pipeline automatizado y reproducible  
- Procesamiento diario sin intervención humana  
- Logs persistentes  
- Manejo robusto de errores  
- Datos limpios en PostgreSQL listos para análisis  

El dashboard no forma parte de esta versión del proyecto.

---





