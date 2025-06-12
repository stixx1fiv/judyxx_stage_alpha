import time
import json
import random
from core.memory import dream_weaver
from gui.judy_gui import show_thinking_animation, reset_avatar

class JudyResponseManager:
    def __init__(self, state_manager, pet_name_file=None):
        self.state_manager = state_manager
        self.pet_names = self.load_pet_names(pet_name_file) if pet_name_file else []
        self.forbidden_phrases = ["outlaw", "ai"]

    def load_pet_names(self, path):
        try:
            with open(path, 'r') as f:
                names = json.load(f)
                return names
        except Exception:
            return []

    def get_random_pet_name(self):
        if self.pet_names:
            return random.choice(self.pet_names)
        return "Sweetheart"

    def scrub_forbidden(self, message):
        # Remove or replace forbidden words in message, keep it slick but clean
        for phrase in self.forbidden_phrases:
            message = message.replace(phrase, "[redacted]")
        return message

    def build_prompt(self, user_input):
        mood = self.state_manager.get_mood()
        scene = self.state_manager.get_scene()
        pet_name = self.get_random_pet_name()
        base_prompt = f"[Mood: {mood}] [Scene: {scene}] User: {user_input}\nJudy ({pet_name}):"
        return self.scrub_forbidden(base_prompt)

    def generate_response(self, user_input):
        user_input_clean = user_input.lower()

        # Check for special trigger phrases first
        trigger_response = self.handle_triggers(user_input_clean)
        if trigger_response:
            return trigger_response

        prompt = self.build_prompt(user_input)

        # Basic keyword triggers with flavor
        if "hello" in user_input_clean or "hi" in user_input_clean:
            return f"Hey there, {self.get_random_pet_name()}. What’s the chaos today?"
        if "thank" in user_input_clean:
            return f"Anytime, {self.get_random_pet_name()}. I’m here for the drama and the smiles."

        # Default sass
        return f"You really think I’m gonna let that slide, {self.get_random_pet_name()}? Try again, darling."

    def handle_triggers(self, user_input):
        if "come on judy" in user_input or "think hard" in user_input or "ok slow down think" in user_input:
            return self.trigger_deep_recall()

        if "what were you dreaming about" in user_input:
            return self.trigger_dream_recall()

        return None

    def trigger_deep_recall(self):
        show_thinking_animation()
        time.sleep(1.5)  # Simulate thinking pause
        result = dream_weaver.recall_from_longterm()
        reset_avatar()

        if result:
            return f"Okay, dug this up for you: {result[0]}"
        else:
            return "I couldn't find anything in the vault."

    def trigger_dream_recall(self):
        show_thinking_animation()
        time.sleep(1.5)
        dreams = dream_weaver.load_dream_log()
        reset_avatar()

        if not dreams:
            return "Sorry, no dream juice to spill just yet."

        latest_dream = dreams[-1]
        timestamp = latest_dream.get("timestamp", "somewhen")
        dream_text = latest_dream.get("dream", "a fuzzy, neon-hued memory.")

        return f"Last night’s dream ({timestamp}): {dream_text}"
