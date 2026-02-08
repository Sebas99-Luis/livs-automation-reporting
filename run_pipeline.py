import os
import sys
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Añadir carpeta src al path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_PATH = os.path.join(BASE_DIR, "src")
sys.path.append(SRC_PATH)

# Importar módulos del pipeline
from ingest.detect_files import get_incoming_files
from ingest.read_csv import read_csv_file
from clean.clean_record import clean_dataframe
from load.db_connection import get_connection
from load.upsert_sales import upsert_sales
from file_handling.move_files import move_file, write_log


def process_file(filepath):
    filename = os.path.basename(filepath)

    try:
        # Leer archivo
        df, missing = read_csv_file(filepath)

        # Limpiar datos
        clean_df = clean_dataframe(df)

        # Cargar en Postgres
        conn = get_connection()
        upsert_sales(clean_df, conn)
        conn.close()

        # Mover archivo a processed
        move_file(filepath, "ok")

        # Registrar log
        write_log(filename, len(df), len(clean_df), "none")

        print(f"✔ Procesado correctamente: {filename}")

    except Exception as e:
        # Mover archivo a bad
        move_file(filepath, "bad")

        # Registrar log con error
        write_log(filename, len(df) if "df" in locals() else 0, 0, str(e))

        print(f"✖ Error procesando {filename}: {e}")


def main():
    files = get_incoming_files()

    if not files:
        print("No hay archivos en data/incoming/.")
        return

    for filepath in files:
        process_file(filepath)

    print("Pipeline finalizado.")


if __name__ == "__main__":
    main()