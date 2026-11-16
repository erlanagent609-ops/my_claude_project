import sys
import os

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.command_runner import run_command

def main():
    print("Executor Agent: Initiating workspace sync to GitHub...")
    success = run_command(["python3", "scripts/git_sync.py"])
    if success:
        print("Workspace sync completed successfully via Executor Agent!")
    else:
        print("Workspace sync encountered issues.")

if __name__ == "__main__":
    main()
