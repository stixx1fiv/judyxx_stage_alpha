import os
import sys
import json
from PyQt5.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QHBoxLayout, QSlider,
    QPushButton, QCheckBox, QApplication, QMessageBox,
    QLineEdit, QFileDialog
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

STATE_PATH = "config/judy_state.json"
CONFIG_PATH = "config/judy_config.json"
MOOD_IMAGE_PATH = "assets/images/moods/"

def load_json(path):
    with open(path, "r") as f:
        return json.load(f)

def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

class SettingsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Judy Settings")
        self.setGeometry(300, 300, 600, 500)
        self.setStyleSheet("background-color: #111; color: white;")
        self.state = load_json(STATE_PATH)
        self.config = load_json(CONFIG_PATH)

        layout = QVBoxLayout()

        # === Mood Sliders ===
        self.sliders = {}
        for trait in ["sarcasm", "playfulness", "affection", "flirty_edge"]:
            hbox = QHBoxLayout()
            label = QLabel(f"{trait.capitalize()}:")
            label.setFont(QFont("Arial", 10))
            slider = QSlider(Qt.Horizontal)
            slider.setMinimum(0)
            slider.setMaximum(100)
            slider.setValue(int(self.state["traits"].get(trait, 0) * 100))
            slider.valueChanged.connect(self.update_state)
            self.sliders[trait] = slider
            hbox.addWidget(label)
            hbox.addWidget(slider)
            layout.addLayout(hbox)

        # === Active Model Path Field ===
        layout.addWidget(QLabel("Active LLM Model Path:"))
        self.model_path_field = QLineEdit()
        self.model_path_field.setText(self.config.get("model_path", ""))
        layout.addWidget(self.model_path_field)

        browse_btn = QPushButton("Browse…")
        browse_btn.clicked.connect(self.browse_model_path)
        layout.addWidget(browse_btn)

        # === Force Mode Buttons ===
        force_layout = QHBoxLayout()
        for mode in ["Work", "Sam", "Spicy"]:
            btn = QPushButton(f"Force {mode}")
            btn.clicked.connect(lambda checked, m=mode: self.force_mode(m))
            force_layout.addWidget(btn)
        layout.addLayout(force_layout)

        # === Developer Mode Toggle ===
        self.dev_toggle = QCheckBox("Developer Mode")
        self.dev_toggle.setChecked(self.state.get("dev_mode", False))
        self.dev_toggle.stateChanged.connect(lambda state: self.set_state("dev_mode", bool(state)))
        layout.addWidget(self.dev_toggle)

        # === Save, Reboot & Close Buttons ===
        button_layout = QHBoxLayout()
        save_btn = QPushButton("Save")
        save_btn.clicked.connect(self.save_and_close)
        reboot_btn = QPushButton("Reboot")
        reboot_btn.clicked.connect(self.reboot_app)
        close_btn = QPushButton("Cancel")
        close_btn.clicked.connect(self.close)
        button_layout.addWidget(save_btn)
        button_layout.addWidget(reboot_btn)
        button_layout.addWidget(close_btn)
        layout.addLayout(button_layout)

        self.setLayout(layout)

    def update_state(self):
        for trait, slider in self.sliders.items():
            self.state["traits"][trait] = slider.value() / 100.0

    def set_state(self, key, value):
        self.state[key] = value

    def browse_model_path(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select Model File", "", "Model Files (*.bin *.gguf);;All Files (*)"
        )
        if file_path:
            self.model_path_field.setText(file_path)
            self.config["model_path"] = file_path
            save_json(CONFIG_PATH, self.config)
            print(f"✅ Model path updated to: {file_path}")

    def force_mode(self, mode):
        self.state["forced_mode"] = mode.lower()
        save_json(STATE_PATH, self.state)
        QMessageBox.information(self, "Mode Forced", f"Judy will enter {mode} Mode next launch.")
        print(f"💥 Forced mode: {mode}")

    def save_and_close(self):
        self.update_state()
        self.config["model_path"] = self.model_path_field.text()
        save_json(STATE_PATH, self.state)
        save_json(CONFIG_PATH, self.config)
        self.close()

    def reboot_app(self):
        self.update_state()
        self.config["model_path"] = self.model_path_field.text()
        save_json(STATE_PATH, self.state)
        save_json(CONFIG_PATH, self.config)
        QMessageBox.information(self, "Rebooting", "Judy is rebooting now…")
        print("🔄 Rebooting Judy…")
        os.execl(sys.executable, sys.executable, *sys.argv)

# === For standalone testing ===
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = SettingsWindow()
    win.show()
    sys.exit(app.exec_())
