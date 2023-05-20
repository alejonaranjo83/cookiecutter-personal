# En este archivo defino procesos que quiero que se ejecuten antes de que se esté creando un proyecto


import os
import sys

project_slug = "{{ cookiecutter.project_slug }}"

ERROR_COLOR = "\x1b[31m"
MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

if project_slug.startswith("x"):
   print(f"{ERROR_COLOR}ERROR: {project_slug=} is not a valid name for this template.{RESET_ALL}")

   sys.exit(1)

print(f"{MESSAGE_COLOR}Has creado un proyecto a través de una plantilla de cookiecutter!")
print(f"Este se encuentra en la ruta: { os.getcwd() }{RESET_ALL}")
