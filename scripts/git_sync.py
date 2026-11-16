import subprocess

def git_sync():
    repo_url = "https://github.com/erlanagent609-ops/my_claude_project.git"
    print(f"Target repository: {repo_url}")
    try:
        print("Running git add .")
        subprocess.run(["git", "add", "."], check=True)
        
        print("Running git commit")
        subprocess.run(["git", "commit", "-m", "chore: autonomous multi-agent sync"], check=False)
        
        print("Running git push origin main")
        result = subprocess.run(["git", "push", "origin", "main"], capture_output=True, text=True, check=True)
        print("Git push successful:", result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Git sync completed or handled with message: {e.stderr}")

if __name__ == "__main__":
    git_sync()
