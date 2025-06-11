import json

class SceneManager:
    def __init__(self, scene_file="conscience_state.json"):
        self.scene_file = scene_file
        self.state = {}
        self.load_scene()

    def load_scene(self):
        try:
            with open(self.scene_file, "r") as f:
                self.state = json.load(f)
        except FileNotFoundError:
            self.state = {}

    def get_scene(self):
        return self.state.get("scene", "DEFAULT")

    def update_scene(self, new_scene):
        self.state["scene"] = new_scene
        with open(self.scene_file, "w") as f:
            json.dump(self.state, f, indent=2)
