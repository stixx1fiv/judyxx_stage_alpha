import json
import threading
import time
from datetime import datetime
from collections import Counter
from textblob import TextBlob

LOG_PATH = "config/subconscious_log.json"
PROFILE_PATH = "config/personality_bias.json"

def load_json(path):
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except:
        return {}

def save_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)

def log_event(source, message):
    log = load_json(LOG_PATH)
    log.setdefault("events", []).append({
        "timestamp": datetime.now().isoformat(),
        "source": source,
        "message": message,
        "sentiment": TextBlob(message).sentiment.polarity
    })
    save_json(LOG_PATH, log)

def evaluate_patterns():
    log = load_json(LOG_PATH)
    messages = [event["message"] for event in log.get("events", [])]
    word_counts = Counter(" ".join(messages).lower().split())

    # Filter words with frequency > 3 and length > 3
    common_words = {word: count for word, count in word_counts.items() if count > 3 and len(word) > 3}

    profile = load_json(PROFILE_PATH)
    profile["frequent_topics"] = common_words
    save_json(PROFILE_PATH, profile)

def subconscious_loop():
    while True:
        time.sleep(300)  # every 5 minutes
        evaluate_patterns()

def start_subconscious():
    thread = threading.Thread(target=subconscious_loop, daemon=True)
    thread.start()
