class JudyResponseManager:
    def __init__(self, state_manager):
        self.state_manager = state_manager

    def build_prompt(self, user_input):
        mood = self.state_manager.get_mood()
        scene = self.state_manager.get_scene()
        return f"[Mood: {mood}] [Scene: {scene}] User: {user_input}\nJudy:"

    def generate_response(self, prompt):
        # Simulated response logic
        if "hello" in prompt.lower():
            return "Hey there, sugar. What’s the chaos today?"
        return "You really think I’m gonna let that slide? Try again, darling."