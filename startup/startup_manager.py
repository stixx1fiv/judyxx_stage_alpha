# core/startup_manager.py

from core.memory.memory_manager import MemoryManager
from core.memory.subconscious_manager import start_subconscious
from core.memory.dream_weaver import start_dream_mode

class StartupManager:
    def __init__(self):
        self.memory_manager = None

    def start(self):
        print("[Startup] Booting Judy...")
        self.memory_manager = MemoryManager()
        print("[Startup] Memory Manager loaded.")
        
        start_subconscious()
        print("[Startup] Subconscious Logger started.")
        
        start_dream_mode()
        print("[Startup] Dream Mode activated.")
        
        # Initialize other systems here like mood, scene, GUI launch
        
        print("[Startup] Judy is ready to roll.")

if __name__ == "__main__":
    sm = StartupManager()
    sm.start()
