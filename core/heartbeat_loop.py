import threading
import time
from gui.judy_gui import set_heartbeat_color, reset_heartbeat_color

class HeartbeatLoop:
    def __init__(self, judy_engine_instance, interval=20):
        self.judy = judy_engine_instance  # Inject JudyEngine instance here
        self.interval = interval          # seconds between subconscious cycles
        self.running = False
        self.thread = None

    def start(self):
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self._run_loop, daemon=True)
            self.thread.start()

    def stop(self):
        self.running = False
        if self.thread:
            self.thread.join()

    def _run_loop(self):
        while self.running:
            # Signal Judy is deep thinking by changing heartbeat color
            set_heartbeat_color("blue")  

            # Run Judy's slow brain process for background memory work
            self.judy.slow_brain_process()

            # Back to normal heartbeat color, thinking done
            reset_heartbeat_color()

            # Wait for the next heartbeat cycle
            time.sleep(self.interval)
