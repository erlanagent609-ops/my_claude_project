import os
import sys

sys.path.append(os.path.dirname(__file__))
from report_progress import report_today_progress
from git_pusher_agent import git_pusher_agent

if __name__ == "__main__":
    print("Running Notification Reporter Agent...")
    report_today_progress()
    print("Running Git Pusher Agent...")
    git_pusher_agent()
    print("All tasks completed.")
