import os
import shutil

# Path to the custom prepare-commit-msg hook (source)
hook_source = os.path.join(os.getcwd(), "prepare-commit-msg")

# Path to the .git/hooks/ directory (destination)
hook_destination = os.path.join(os.getcwd(), ".git/hooks/prepare-commit-msg")

# Copy the hook to the Git hooks directory
if os.path.exists(hook_source):
    shutil.copyfile(hook_source, hook_destination)
    os.chmod(hook_destination, 0o755)
    print("Git hook installed successfully!")
else:
    print(f"Hook source file not found: {hook_source}")
