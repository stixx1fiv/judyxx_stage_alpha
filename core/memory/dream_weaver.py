import threading
import time
import random
import json
from datetime import datetime

DREAM_LOG = "config/dream_log.json"

def load_dream_log():
    try:
        with open(DREAM_LOG, 'r') as f:
            return json.load(f)
    except:
        return []

def save_dream_log(dreams):
    with open(DREAM_LOG, 'w') as f:
        json.dump(dreams, f, indent=2)

def generate_dream():
    themes = [
        "neon city streets at midnight",
        "whispers of forgotten secrets",
        "a storm of glowing butterflies",
        "the hum of distant engines",
        "a dance beneath shattered stars",
        "a tangled web of memories",
        "the echo of laughter in a dark alley"
    ]
    chosen = random.choice(themes)
    timestamp = datetime.now().isoformat()
    dream_entry = {"timestamp": timestamp, "dream": f"Judy dreams of {chosen}."}
    return dream_entry

def dream_loop():
    dreams = load_dream_log()
    while True:
        time.sleep(random.randint(600, 1200))  # 10 to 20 minutes between dreams
        new_dream = generate_dream()
        dreams.append(new_dream)
        save_dream_log(dreams)
        print(f"[DreamWeaver] Dream logged: {new_dream['dream']}")

def start_dream_mode():
    thread = threading.Thread(target=dream_loop, daemon=True)
    thread.start()
