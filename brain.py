import time

class JudyBrain:
    def __init__(self):
        self.current_mood = "neutral"
        self.scene = "DEFAULT"

    def process_input(self, input_text):
        # Placeholder logic: mood shift based on input
        if "happy" in input_text.lower():
            self.current_mood = "playful"
            self.scene = "NEON_ALLEY"
        elif "work" in input_text.lower():
            self.current_mood = "focused"
            self.scene = "OFFICE"
        else:
            self.current_mood = "neutral"
            self.scene = "DEFAULT"

    def get_state(self):
        return {"mood": self.current_mood, "scene": self.scene}

    def think_loop(self):
        # Simulate Judy thinking idly and updating state
        while True:
            print(f"[JudyBrain] Mood: {self.current_mood}, Scene: {self.scene}")
            time.sleep(5)
