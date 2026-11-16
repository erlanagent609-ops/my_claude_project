import sys
import os

sys.path.append(os.path.dirname(__file__))
from git_pusher_agent import git_pusher_agent

if __name__ == "__main__":
    git_pusher_agent()
