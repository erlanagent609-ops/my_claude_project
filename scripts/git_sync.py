import subprocess
import json
import os

def git_sync():
    config_path = "config/git_credentials.json"
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

    print(f"Target repository configured.")
    try:
        print("Setting remote URL...")
        subprocess.run(["git", "remote", "set-url", "origin", repo_url], check=True)

        print("Running git add .")
        subprocess.run(["git", "add", "."], check=True)
        
        print("Running git commit")
        subprocess.run(["git", "commit", "-m", "chore: autonomous multi-agent sync with credentials"], check=False)
        
        print("Running git push origin main")
        result = subprocess.run(["git", "push", "origin", "main"], capture_output=True, text=True, check=True)
        print("Git push successful:", result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Git sync encountered an error: {e.stderr}")

if __name__ == "__main__":
    git_sync()
