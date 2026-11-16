import os
import sys

# Ensure project root is in path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts.git_pusher_agent import git_pusher_agent, log_activity

def test_pusher():
    print("Testing Git Pusher Agent...")
    log_activity("Running test for Git Pusher Agent.")
    try:
        # Run the agent function (dry-run or status check)
        git_pusher_agent()
        print("Git Pusher Agent test executed successfully.")
    except Exception as e:
        print(f"Test failed with error: {e}")

if __name__ == "__main__":
    test_pusher()
