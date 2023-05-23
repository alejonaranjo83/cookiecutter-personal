# This file defines processes that I want to execute once the project has been created


import os
import subprocess

MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

print(f"{MESSAGE_COLOR}Almost ready!")
print(f"Initializing a git repository...{RESET_ALL}")

subprocess.call(['git', 'init']) #Create a repository
subprocess.call(['git', 'add', '*']) # Add files to stagging
subprocess.call(['git', 'commit', '-m', 'Initial commit']) #Create the first commit

print(f"{MESSAGE_COLOR}You're ready to start your project!{RESET_ALL}")