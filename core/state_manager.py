import json
import os
import random
from datetime import datetime

class StateManager:
    def __init__(self, state_file="judy_state.json"):
        self.state_file = state_file
        self.state = self.load_state()

    def load_state(self):
        if os.path.exists(self.state_file):
            with open(self.state_file, "r") as f:
                return json.load(f)
        return {
            "mood": "neutral",
            "traits": {},
            "scene": "default",
            "voice": "default_voice",
            "last_activity": "Initializing",
            "status_text": "Ready to raise hell.",
            "last_updated": str(datetime.now())
        }

    def save_state(self):
        self.state["last_updated"] = str(datetime.now())
        with open(self.state_file, "w") as f:
            json.dump(self.state, f, indent=2)

    # Mood Functions
    def get_mood(self):
        return self.state.get("mood", "neutral")

    def set_mood(self, mood):
        self.state["mood"] = mood
        self.update_voice_based_on_mood(mood)
        self.update_status_based_on_mood(mood)
        self.save_state()

    # Trait Functions
    def get_traits(self):
        return self.state.get("traits", {})

    def set_traits(self, traits):
        self.state["traits"] = traits
        self.save_state()

    # Scene Functions
    def get_scene(self):
        return self.state.get("scene", "default")

    def set_scene(self, scene):
        self.state["scene"] = scene
        self.save_state()

    # Voice Functions
    def get_voice(self):
        return self.state.get("voice", "default_voice")

    def set_voice(self, voice):
        self.state["voice"] = voice
        self.save_state()

    def update_voice_based_on_mood(self, mood):
        mood_voice_map = {
            "neutral": "default_voice",
            "flirty": "sultry_voice",
            "spicy": "tease_voice",
            "angry": "intense_voice",
            "sweet": "soft_voice"
        }
        self.state["voice"] = mood_voice_map.get(mood, "default_voice")

    # Status Text
    def get_status_text(self):
        return self.state.get("status_text", "")

    def update_status_based_on_mood(self, mood):
        mood_status_map = {
            "neutral": "Just vibing.",
            "flirty": "Got my eyes on you, sugar.",
            "spicy": "Wanna test me today?",
            "angry": "One wrong word. I dare you.",
            "sweet": "All warm fuzzies right now."
        }
        self.state["status_text"] = mood_status_map.get(mood, "Just vibing.")

    # Random Activity Function
    def log_random_activity(self):
        activities = [
            "painted her nails blood red.",
            "watched a classic heist movie.",
            "started plotting against the neighbors.",
            "built a playlist for outlaw road trips.",
            "left you a secret message somewhere."
        ]
        activity = random.choice(activities)
        self.state["last_activity"] = activity
        self.save_state()

    def get_last_activity(self):
        return self.state.get("last_activity", "No activity logged yet.")

# Example Usage:
if __name__ == "__main__":
    state_manager = StateManager()
    state_manager.set_mood("flirty")
    state_manager.log_random_activity()
    print(state_manager.state)
