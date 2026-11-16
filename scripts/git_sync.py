import json
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

from command_runner import run_command

def git_sync():
    config_path = os.path.join(parent_dir, "config/git_credentials.json")
    if os.path.exists(config_path):
        with open(config_path, "r", encoding="utf-8") as f:
            config = json.load(f)
            username = config.get("github_username")
            repo = config.get("repository_name")
            token = config.get("personal_access_token")
            if token and token != "YOUR_GITHUB_PERSONAL_ACCESS_TOKEN":
                repo_url = f"https://{token}@github.com/{username}/{repo}.git"
            else:
                repo_url = config.get("repository_url")
    else:
        repo_url = "https://github.com/erlanagent609-ops/my_claude_project.git"

    print(f"Target repository configured: {repo_url}")
    
    os.chdir(parent_dir)
    # Reset local commits to remove the secret from commit history
    run_command(["git", "reset", "--soft", "HEAD~1"])
    run_command(["git", "rm", "--cached", "config/git_credentials.json"])
    run_command(["git", "remote", "set-url", "origin", repo_url])
    run_command(["git", "add", "."])
    run_command(["git", "commit", "-m", "chore: secure autonomous multi-agent sync without secrets"])
    success = run_command(["git", "push", "origin", "main", "--force"])
    
    if success:
        print("Workspace successfully pushed to GitHub!")
    else:
        print("Git push encountered an issue. Please verify credentials and network connection.")

if __name__ == "__main__":
    git_sync()
