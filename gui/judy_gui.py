import sys
import json
import threading
from datetime import datetime
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QVBoxLayout, QHBoxLayout, QScrollArea
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from llama_cpp import Llama

# === Load and Save JSON ===
def load_json(path):
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Failed to load JSON from {path}: {e}")
        return {}

def save_json(path, data):
    try:
        with open(path, 'w') as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        print(f"Failed to save JSON to {path}: {e}")

# === Paths ===
STATE_PATH = "core/memory/judy_state.json"
MEMORY_PATH = "core/memory/memory.json"
MODEL_PATH = "core/models/mythomax-l2-13b.Q5_0.gguf"
AVATAR_IMAGE_PATH = "assets/images/Afternoon Stroll in Cozy Sweater.png"

# === Load State and Memory ===
judy_state = load_json(STATE_PATH)
memory = load_json(MEMORY_PATH)
judy_state["last_contact"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
save_json(STATE_PATH, judy_state)

# === Initialize LLaMA ===
llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=2048,
    n_threads=8,
    n_gpu_layers=35
)

# === TTS placeholder ===
def speak(text):
    # Replace this with your TTS call later
    print(f"[VOICE] {text}")

# === Chat Bubble ===
class ChatBubble(QLabel):
    def __init__(self, text, is_user=False):
        super().__init__(text)
        self.setWordWrap(True)
        self.setStyleSheet(
            f"""
            background-color: {'#2E2E2E' if is_user else '#1C1C1C'};
            color: white;
            padding: 12px;
            border-radius: 12px;
            font-family: 'Courier New';
            font-size: 13px;
            """
        )
        self.setMaximumWidth(420)

# === Main GUI ===
class JudyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("JUDYXX Alpha")
        self.setGeometry(100, 100, 1280, 720)
        self.setStyleSheet("background-color: black;")

        layout = QHBoxLayout(self)

        # === Left panel: Avatar ===
        avatar_label = QLabel()
        pixmap = QPixmap(AVATAR_IMAGE_PATH).scaled(720, 720, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        avatar_label.setPixmap(pixmap)
        layout.addWidget(avatar_label, 3)

        # === Right panel: Chat + input ===
        right_panel = QVBoxLayout()

        self.mood_label = QLabel(f"Mood: {judy_state.get('mood', 'unknown')}")
        self.mood_label.setStyleSheet("color: #888; font-size: 12px; padding: 4px;")
        right_panel.addWidget(self.mood_label)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.chat_container = QVBoxLayout()
        chat_widget = QWidget()
        chat_widget.setLayout(self.chat_container)
        self.scroll_area.setWidget(chat_widget)

        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Say something to Judy...")
        self.input_field.setStyleSheet("background-color: #111; color: white; padding: 12px; font-size: 14px;")
        self.input_field.returnPressed.connect(self.handle_input)

        right_panel.addWidget(self.scroll_area)
        right_panel.addWidget(self.input_field)
        layout.addLayout(right_panel, 2)

        self.show_intro()
        self.start_background_thread()

    def show_intro(self):
        mood = judy_state.get("mood", "neutral")
        line = "Back so soon? Miss me, did you?" if mood == "playful" else "You're back. Let's pick up where we left off."
        self.add_message("Judy", line)
        speak(line)

    def add_message(self, sender, text):
        bubble = ChatBubble(text, is_user=(sender == "You"))
        self.chat_container.addWidget(bubble)
        self.scroll_area.verticalScrollBar().setValue(self.scroll_area.verticalScrollBar().maximum())

    def handle_input(self):
        user_text = self.input_field.text().strip()
        if not user_text:
            return

        self.add_message("You", user_text)
        self.input_field.clear()

        prompt = f"### Instruction:\n{user_text}\n### Response:"
        try:
            response = llm(prompt, max_tokens=200)
            reply = response["choices"][0]["text"].strip()
        except Exception as e:
            reply = f"Oops, something went wrong with LLaMA: {e}"

        self.add_message("Judy", reply)
        speak(reply)

        memory.setdefault("log", []).append({
            "timestamp": datetime.now().isoformat(),
            "user": user_text,
            "judy": reply
        })
        save_json(MEMORY_PATH, memory)

    def start_background_thread(self):
        def background_task():
            import time
            while True:
                print("Judy is thinking in the background...")
                time.sleep(60)
        threading.Thread(target=background_task, daemon=True).start()

# === Run App ===
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = JudyApp()
    window.show()
    sys.exit(app.exec_())
