# En este archivo defino procesos que quiero que se ejecuten después de que se haber creado un proyecto


import os
import subprocess

MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

print(f"{MESSAGE_COLOR}Casi listos!")
print(f"Inicializando un repositorio de git...{RESET_ALL}")

subprocess.call(['git', 'init']) #Crea repositorio
subprocess.call(['git', 'add', '*']) #Añade todos los archivos a stagging
subprocess.call(['git', 'commit', '-m', 'Initial commit']) #Crea el primer commit

print(f"{MESSAGE_COLOR}Estás listo para empezar tu proyecto!{RESET_ALL}")