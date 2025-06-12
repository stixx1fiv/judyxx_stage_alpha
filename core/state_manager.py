import json
import os
import random
from datetime import datetime

class StateManager:
    def __init__(self,
                 state_file="config/judy_state.json",
                 moods_file="config/moods.json",
                 personality_file="config/personality_bias.json"):
        self.state_file = state_file
        self.moods_file = moods_file
        self.personality_file = personality_file

        self.moods = self.load_json(self.moods_file, default={})
        self.personality = self.load_json(self.personality_file, default={})

        self.state = self.load_state()

    def load_json(self, filepath, default):
        if os.path.exists(filepath):
            with open(filepath, "r") as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    print(f"Warning: JSON decode error in {filepath}")
                    return default
        else:
            return default

    def load_state(self):
        if os.path.exists(self.state_file):
            with open(self.state_file, "r") as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    print(f"Warning: JSON decode error in {self.state_file}, resetting state.")
        # Default state structure:
        return {
            "mood": "neutral",
            "traits": self.personality,  # load from personality bias
            "scene": "default",
            "voice": self.moods.get("neutral", {}).get("voice", "default_voice"),
            "status_text": self.moods.get("neutral", {}).get("status", "Just vibing."),
            "last_activity": "Initializing",
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
        if mood not in self.moods:
            print(f"Mood '{mood}' not found in moods.json, defaulting to neutral.")
            mood = "neutral"

        self.state["mood"] = mood
        mood_data = self.moods[mood]
        self.state["voice"] = mood_data.get("voice", "default_voice")
        self.state["status_text"] = mood_data.get("status", "Just vibing.")
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

    # Status Text
    def get_status_text(self):
        return self.state.get("status_text", "")

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

# Example quick test usage
if __name__ == "__main__":
    sm = StateManager()
    sm.set_mood("flirty")
    sm.log_random_activity()
    print(sm.state)
