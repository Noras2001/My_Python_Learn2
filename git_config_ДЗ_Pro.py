# Импортируем библиотеку subprocess

# Определяем функцию git_config_list, которая будет выполнять команду Git 
# (нужно в консоль вывести результат работы команды git: git config --global --list)
import subprocess
def git_config_list():
    """
    Определяем функцию, которая будет выполнять команду Git: 
    git config --global --list
    """
    result = subprocess.run(['git', 'config', '--global', '--list'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    if result.returncode == 0:
        print(result.stdout)
    else:
        print("Error al ejecutar el comando:", result.stderr)

git_config_list()
