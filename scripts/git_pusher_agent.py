import subprocess
import os
from datetime import datetime

def log_activity(message):
    log_path = os.path.join(os.path.dirname(__file__), '../git_push_activity.log')
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}\n"
    with open(log_path, 'a', encoding='utf-8') as f:
        f.write(log_entry)
    print(log_entry.strip())

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
    
    # 1. Check git status
    success, stdout = run_command(["git", "status"])
    if not success:
        log_activity(f"Failed to check git status: {stdout}")
        return
    log_activity(f"Git Status:\n{stdout}")
    
    # 2. Ensure sensitive files are ignored
    gitignore_path = os.path.join(root_dir, '.gitignore')
    ignore_entry = "config/git_credentials.json"
    if os.path.exists(gitignore_path):
        with open(gitignore_path, 'r', encoding='utf-8') as f:
            content = f.read()
        if ignore_entry not in content:
            with open(gitignore_path, 'a', encoding='utf-8') as f:
                f.write(f"\n{ignore_entry}\n")
            log_activity("Added config/git_credentials.json to .gitignore.")
            
    # Remove from git cache if tracked
    run_command(["git", "rm", "--cached", "config/git_credentials.json"])
    
    # 3. Git add, commit with dynamic timestamp, and push
    success, stdout = run_command(["git", "add", "."])
    if not success:
        log_activity(f"Git add failed: {stdout}")
        return
        
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    commit_msg = f"Auto-push update oleh agen pada {current_time}"
    
    success, stdout = run_command(["git", "commit", "-m", commit_msg])
    if not success and "nothing to commit" not in stdout:
        log_activity(f"Git commit failed: {stdout}")
        
    success, stdout = run_command(["git", "push", "origin", "main"])
    if success:
        log_activity("Git push successful!")
    else:
        log_activity(f"Git push failed: {stdout}")

if __name__ == "__main__":
    git_pusher_agent()
