import subprocess
import os
from datetime import datetime
import urllib.request
import json

def log_activity(message):
    log_path = os.path.join(os.path.dirname(__file__), '../git_push_activity.log')
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}\n"
    with open(log_path, 'a', encoding='utf-8') as f:
        f.write(log_entry)
    print(log_entry.strip())

def send_notification(message):
    """
    Reporting module for Telegram Bot API & WhatsApp Gateway alerts.
    """
    log_activity(f"[Notification Gateway] Sending alert: {message}")
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID")
    if token and chat_id:
        try:
            url = f"https://api.telegram.org/bot{token}/sendMessage"
            payload = json.dumps({"chat_id": chat_id, "text": message}).encode('utf-8')
            req = urllib.request.Request(url, data=payload, headers={'Content-Type': 'application/json'})
            with urllib.request.urlopen(req) as response:
                if response.status == 200:
                    log_activity("Telegram notification sent successfully.")
        except Exception as e:
            log_activity(f"Failed to send Telegram notification: {e}")
    else:
        log_activity("Telegram credentials not configured. Notification logged locally.")

def run_command(cmd):
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, e.stderr

def git_pusher_agent():
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    os.chdir(root_dir)
    
    log_activity("Git Pusher Agent initiated.")
    
    # 1. Ensure sensitive files are ignored and untracked
    gitignore_path = os.path.join(root_dir, '.gitignore')
    ignore_entry = "config/git_credentials.json"
    if os.path.exists(gitignore_path):
        with open(gitignore_path, 'r', encoding='utf-8') as f:
            content = f.read()
        if ignore_entry not in content:
            with open(gitignore_path, 'a', encoding='utf-8') as f:
                f.write(f"\n{ignore_entry}\n")
            log_activity("Added config/git_credentials.json to .gitignore.")
            
    # Safely untrack sensitive file if it was previously tracked
    run_command(["git", "rm", "--cached", "config/git_credentials.json"])
    
    # 2. Check git status
    success, stdout = run_command(["git", "status"])
    if not success:
        msg = f"Failed to check git status: {stdout}"
        log_activity(msg)
        send_notification(msg)
        return
    log_activity(f"Git Status checked successfully.")
    
    # 3. Git add all changes (excluding ignored files)
    success, stdout = run_command(["git", "add", "."])
    if not success:
        msg = f"Git add failed: {stdout}"
        log_activity(msg)
        send_notification(msg)
        return
        
    # 4. Commit with dynamic timestamp
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    commit_msg = f"Auto-push update oleh agen pada {current_time}"
    
    success, stdout = run_command(["git", "commit", "-m", commit_msg])
    if not success and "nothing to commit" not in stdout:
        msg = f"Git commit failed or nothing to commit: {stdout}"
        log_activity(msg)
    else:
        log_activity("Git commit created successfully.")
        
    # 5. Git push origin main
    success, stdout = run_command(["git", "push", "origin", "main"])
    if success:
        msg = f"Git push successful! Timestamp: {current_time}"
        log_activity(msg)
        send_notification(msg)
    else:
        msg = f"Git push failed: {stdout}"
        log_activity(msg)
        send_notification(msg)

if __name__ == "__main__":
    git_pusher_agent()
