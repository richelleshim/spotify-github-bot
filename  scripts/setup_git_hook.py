import os
import shutil

# Path to your project's prepare-commit-msg file
hook_source = os.path.join(os.getcwd(), "prepare-commit-msg")
# Path to the Git hooks directory
hook_destination = os.path.join(os.getcwd(), ".git/hooks/prepare-commit-msg")

# Copy the hook to the Git hooks directory
shutil.copyfile(hook_source, hook_destination)
os.chmod(hook_destination, 0o755)

print("Git hook installed successfully!")
