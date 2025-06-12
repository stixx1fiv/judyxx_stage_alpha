# core/memory/memory_manager.py

import json
import os

MEMORY_FILE = "config/memory.json"

class MemoryManager:
    def __init__(self):
        self.memory = self.load_memory()

    def load_memory(self):
        if os.path.exists(MEMORY_FILE):
            with open(MEMORY_FILE, 'r') as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return {}
        return {}

    def save_memory(self):
        with open(MEMORY_FILE, 'w') as f:
            json.dump(self.memory, f, indent=2)

    def add_memory(self, key, value):
        self.memory[key] = value
        self.save_memory()

    def get_memory(self, key):
        return self.memory.get(key)

    def clear_memory(self):
        self.memory = {}
        self.save_memory()
