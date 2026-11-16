import os
import sys

sys.path.append(os.path.dirname(__file__))
from git_pusher_agent import send_notification, log_activity

def report_today_progress():
    progress_path = os.path.join(os.path.dirname(__file__), '../docs/daily_progress.md')
    if os.path.exists(progress_path):
        with open(progress_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        message = f"Laporan Progres Harian:\n\n{content[:1000]}..."
        log_activity("Mengirim laporan progres harian ke Telegram dan WhatsApp...")
        send_notification(message)
    else:
        log_activity("File daily_progress.md tidak ditemukan.")

if __name__ == "__main__":
    report_today_progress()
