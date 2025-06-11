import json
import os
import requests
from datetime import datetime
from base64 import b64decode, b64encode

# Paths
BASE_DIR = "C:/Users/cnorthington/JUDYXX_Test"
STATE_FILE = os.path.join(BASE_DIR, "config/judy_state.json")
BASE_PROFILE = os.path.join(BASE_DIR, "config/judy_base_profile.json")
STYLE_PROFILE = os.path.join(BASE_DIR, "config/judy_style_profile.json")
SCENE_PROFILE = os.path.join(BASE_DIR, "config/judy_scene_profile.json")
PROP_PROFILE = os.path.join(BASE_DIR, "config/prop_profile.json")
OUTPUT_DIR = os.path.join(BASE_DIR, "avatars/judy_default")

os.makedirs(OUTPUT_DIR, exist_ok=True)

def load_json(path):
    with open(path, "r") as f:
        return json.load(f)

def build_prompt(state):
    base = load_json(BASE_PROFILE)
    style = load_json(STYLE_PROFILE)
    scene = load_json(SCENE_PROFILE)
    props = load_json(PROP_PROFILE)

    scene_details = scene.get(state["current_scene"], {}).get("details", "")

    return ", ".join([
        base.get("description", ""),
        f"wearing {state['current_outfit']}",
        f"in a {state['current_scene']} setting",
        f"mood: {state['mood']}",
        style.get("style", ""),
        scene_details,
        props.get("items", "")
    ])

def generate_txt2img(prompt, seed, output_path):
    url = "http://127.0.0.1:7860/sdapi/v1/txt2img"
    payload = {
        "prompt": prompt,
        "seed": seed,
        "steps": 20,
        "cfg_scale": 7,
        "width": 512,
        "height": 512
    }
    response = requests.post(url, json=payload)
    response.raise_for_status()
    image_data = response.json()["images"][0]
    with open(output_path, "wb") as f:
        f.write(b64decode(image_data))

def generate_img2img(prompt, seed, base_image_path, output_path):
    url = "http://127.0.0.1:7860/sdapi/v1/img2img"
    with open(base_image_path, "rb") as f:
        base_image_data = b64encode(f.read()).decode("utf-8")
    payload = {
        "prompt": prompt,
        "seed": seed,
        "steps": 20,
        "cfg_scale": 7,
        "width": 512,
        "height": 512,
        "init_images": [base_image_data],
        "denoising_strength": 0.3
    }
    response = requests.post(url, json=payload)
    response.raise_for_status()
    image_data = response.json()["images"][0]
    with open(output_path, "wb") as f:
        f.write(b64decode(image_data))

if __name__ == "__main__":
    state = load_json(STATE_FILE)
    prompt = build_prompt(state)
    seed = state["seed"]
    filename = f"{state['base_image'].replace('.png', '')}_{state['current_outfit']}_{state['current_scene']}_seed{seed}.png"
    output_path = os.path.join(OUTPUT_DIR, filename)

    # Choose mode: "txt2img" or "img2img"
    mode = "txt2img"  # Change to "img2img" if needed
    base_image_path = os.path.join(BASE_DIR, "judy_ui/assets/judy_idle.png")  # Required for img2img

    print(f"Generating image with prompt:\n{prompt}\nSeed: {seed}")

    if mode == "txt2img":
        generate_txt2img(prompt, seed, output_path)
    elif mode == "img2img":
        generate_img2img(prompt, seed, base_image_path, output_path)
    else:
        print("Invalid mode. Choose 'txt2img' or 'img2img'.")

    print(f"Image saved to {output_path}")
