from state_manager import StateManager
from memory_manager import MemoryManager
from judy_response_manager import JudyResponseManager

class JudyEngine:
    def __init__(self):
        self.state_manager = StateManager()
        self.memory_manager = MemoryManager()
        self.response_manager = JudyResponseManager(self.state_manager)

    def process_input(self, user_input):
        prompt = self.response_manager.build_prompt(user_input)
        response = self.response_manager.generate_response(prompt)
        self.memory_manager.update_memory("last_input", user_input)
        self.memory_manager.update_memory("last_response", response)
        return response