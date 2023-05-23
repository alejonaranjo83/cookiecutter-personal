# This file defines processes that I want to execute before the project is created


import os
import sys

project_slug = "{{ cookiecutter.project_slug }}"

ERROR_COLOR = "\x1b[31m"
MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

if project_slug.startswith("x"):
   print(f"{ERROR_COLOR}ERROR: {project_slug=} is not a valid name for this template.{RESET_ALL}")

   sys.exit(1)

print(f"{MESSAGE_COLOR}You've created a project through a cookiecutter template!")
print(f"This is the route in which the project is contained: { os.getcwd() }{RESET_ALL}")
