from core.startup_manager import StartupManager
from core.judy_response_manager import JudyResponseManager
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from gui.widgets.mood_selector import MoodSelector
from gui.widgets.task_tracker import TaskTracker
from gui.widgets.toggle_controls import ToggleControls
from gui.widgets.chat_box import ChatBox

class JudyRoomScreen(Screen):
    pass

class JudyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(JudyRoomScreen(name='judy_room'))
        return sm

# Assuming you have a state_manager instance from somewhere
response_manager = JudyResponseManager(state_manager, pet_name_file="config/pet_names.json")

# Example usage inside your main loop or message handler:
def handle_user_input(user_input):
    response = response_manager.generate_response(user_input)
    print(response)  # Or send to your GUI text output



def main():
    startup = StartupManager()
    startup.start()
    print("Welcome back, Stixx. Judy is listening...")
    JudyApp().run()
