import os
import shutil

# Old repo path
old_repo = r"C:\Users\cnorthington\JUDY\JUDYXX_Alpha"

# New repo path
new_repo = r"C:\Users\cnorthington\Judyxx"

# New folder structure
folders_to_create = [
    "core",
    "gui",
    "memory",
    "config",
    "logs",
    "assets",
    "tts",
]

# File extensions we want to keep
allowed_extensions = [".py", ".json", ".txt", ".md"]

# Create new directory structure
for folder in folders_to_create:
    os.makedirs(os.path.join(new_repo, folder), exist_ok=True)

# Function to move allowed files
def move_files(src_dir, dest_dir):
    for root, _, files in os.walk(src_dir):
        for file in files:
            if os.path.splitext(file)[1].lower() in allowed_extensions:
                src_path = os.path.join(root, file)
                rel_path = os.path.relpath(src_path, old_repo)
                dest_path = os.path.join(new_repo, rel_path)

                os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                shutil.move(src_path, dest_path)
                print(f"Moved: {rel_path}")

# Move files
move_files(old_repo, new_repo)

print("\n🔥 Done. Judyxx is ready for business.")
