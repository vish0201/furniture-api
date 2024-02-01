import os
import time
import subprocess

n = 100

# Replace the path with the actual path to your Git repository
git_repo_path = r"C:\Users\dvish\react-js\SetOfProjects\furniture-api"

for _ in range(n):
    with open("./data.txt", "a+") as file:
        file.write("hello World\n")

    # Use subprocess.Popen to run the Git command in the terminal
    git_command = "git add . && git commit -m 'Auto-commit' && git push"
    subprocess.Popen(git_command, shell=True)

    time.sleep(10)
