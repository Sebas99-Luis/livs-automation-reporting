import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# Subir dos niveles: src/ingest → src → app
PROJECT_DIR = os.path.dirname(os.path.dirname(CURRENT_DIR))

DATA_DIR = os.path.join(PROJECT_DIR, "data")
INCOMING_DIR = os.path.join(DATA_DIR, "incoming")



def get_incoming_files():
    files = []
    for f in os.listdir(INCOMING_DIR):
        if f.lower().endswith(".csv"):
            full_path = os.path.join(INCOMING_DIR, f)
            if os.path.getsize(full_path) > 0:
                files.append(full_path)
    return files