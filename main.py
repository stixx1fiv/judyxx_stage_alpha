from core.startup_manager import StartupManager
from core.judy_response_manager import JudyResponseManager
# Assuming you have a state_manager instance from somewhere
response_manager = JudyResponseManager(state_manager, pet_name_file="config/pet_names.json")

# Example usage inside your main loop or message handler:
def handle_user_input(user_input):
    response = response_manager.generate_response(user_input)
    print(response)  # Or send to your GUI text output


def main():
    startup = StartupManager()
    startup.start()
    # Your main event loop, GUI launch, or REPL goes here
    print("Welcome back, Stixx . Judy is listening...")

if __name__ == "__main__":
    main()
