import shutil
import os
from datetime import datetime

def move_file(filepath, status):
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(filepath)))
    filename = os.path.basename(filepath)

    processed_dir = os.path.join(base_dir, "data", "processed")
    bad_dir = os.path.join(base_dir, "data", "bad")

    os.makedirs(processed_dir, exist_ok=True)
    os.makedirs(bad_dir, exist_ok=True)

    if status == "ok":
        target = os.path.join(processed_dir, filename)
    else:
        target = os.path.join(bad_dir, filename)

    shutil.move(filepath, target)
    return target


def write_log(filename, rows_read, rows_loaded, errors):
    log_dir = os.path.join(os.getcwd(), "logs")
    os.makedirs(log_dir, exist_ok=True)

    log_path = os.path.join(log_dir, "pipeline.log")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(log_path, "a", encoding="utf-8") as f:
        f.write(
            f"{timestamp} | file={filename} | read={rows_read} | loaded={rows_loaded} | errors={errors}\n"
        )