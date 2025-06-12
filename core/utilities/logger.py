import os
from datetime import datetime

LOG_FILE_PATH = os.path.join("tools", "logs", "activity_log.txt")

def log_event(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{timestamp}] {message}\n"

    os.makedirs(os.path.dirname(LOG_FILE_PATH), exist_ok=True)

    with open(LOG_FILE_PATH, "a") as log_file:
        log_file.write(log_message)

    print(log_message.strip())  # Optional: echo to console for dev
