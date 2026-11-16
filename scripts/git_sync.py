import sys
import os

sys.path.append(os.path.dirname(__file__))
from git_pusher_agent import git_pusher_agent
from report_progress import report_today_progress

if __name__ == "__main__":
    print("Menjalankan Notification Reporter Agent (WhatsApp & Telegram)...")
    report_today_progress()
    print("Menjalankan Git Pusher Agent (GitHub Sync)...")
    git_pusher_agent()
