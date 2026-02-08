import os

INCOMING_DIR = "data/incoming"

def get_incoming_files():
    files = []
    for f in os.listdir(INCOMING_DIR):
        if f.lower().endswith(".csv"):
            full_path = os.path.join(INCOMING_DIR, f)
            if os.path.getsize(full_path) > 0:
                files.append(full_path)
    return files