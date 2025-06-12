from state_manager import StateManager
from memory_manager import MemoryManager
from judy_response_manager import JudyResponseManager
from core.utilities.helper_funcs import embed_and_score_events
from core.utilities.logger import log_event
import time

class JudyEngine:
    def __init__(self):
        self.state_manager = StateManager()
        self.memory_manager = MemoryManager()
        self.response_manager = JudyResponseManager(self.state_manager)
        self.event_queue = []  # Queue for deep, slow processing

    def process_input(self, user_input):
        # Quick front-end reaction
        prompt = self.response_manager.build_prompt(user_input)
        response = self.response_manager.generate_response(prompt)

        # Fast brain updates immediate short-term memory
        self.memory_manager.update_memory("last_input", user_input)
        self.memory_manager.update_memory("last_response", response)

        # Add to slow brain event queue for deep processing
        self.event_queue.append({
            "type": "user_input",
            "content": user_input,
            "timestamp": time.time(),
            "priority": 5  # Priority placeholder — could be extended
        })

        return response

    def slow_brain_process(self):
        """
        Background process called periodically (e.g. heartbeat_loop)
        to embed, score, and store events into long-term memory.
        """

        while self.event_queue:
            event = self.event_queue.pop(0)
            
            # Generate embedding + score for the event content
            embedding, score = embed_and_score_events(event["content"])

            # Store the enriched memory event
            self.memory_manager.store_embedding(event["content"], embedding, score, event["timestamp"])

            # Log the deep thought process for debugging or audits
            log_event(f"Processed event '{event['content']}' with score {score}")

        # Manage memory maintenance tasks (decay, clustering, etc)
        self.memory_manager.run_governor()
