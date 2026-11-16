import subprocess
import sys

def run_command(command_list):
    try:
        print(f"Executing: {' '.join(command_list)}")
        result = subprocess.run(command_list, capture_output=True, text=True, check=True)
        print("--- STDOUT ---")
        print(result.stdout)
        if result.stderr:
            print("--- STDERR ---")
            print(result.stderr)
        return result.returncode == 0
    except subprocess.CalledProcessError as e:
        print(f"Command failed with exit code {e.returncode}")
        print("--- STDOUT ---")
        print(e.stdout)
        print("--- STDERR ---")
        print(e.stderr)
        return False

if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_command(sys.argv[1:])
    else:
        print("Usage: python3 scripts/command_runner.py <command> [args...]")
