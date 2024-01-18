import os
import shutil
import subprocess
from colorama import Fore, init
from socket import gethostname
from getpass import getuser
from prompt_toolkit import prompt
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit import ANSI
import datetime


init(autoreset=True)

"""history = []"""
current_directory = os.getcwd()
current_folder = current_directory.split("\\")[len(current_directory.split("\\"))-1] if current_directory.split("\\")[len(current_directory.split("\\"))-1]!="" else current_directory[:-2]



def inp_pref():
    return f'{Fore.LIGHTGREEN_EX}{getuser()}@{current_folder}{Fore.RESET}:{Fore.LIGHTBLUE_EX}~{Fore.RESET}$ '



def show_directory_contents(directory):
    print(f"Contents of directory '{directory}':")
    list_files(directory)


"""log_file = "command_log.txt"


def log_command(user, command):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a", encoding="utf-8") as log:
        log.write(f"{timestamp} - User: {user}, Command: {command}\n")"""


def move_file(src, dest):
    try:
        shutil.move(src, dest)
        print(f"Moved {src} to {dest}")
    except FileNotFoundError:
        print(f"File not found: {src}")

def move_file_command(src, dest):
    try:
        shutil.move(src, dest)
        print(f"Moved {src} to {dest}")
    except FileNotFoundError:
        print(f"File not found: {src}")

def copy_file(src, dest):
    try:
        shutil.copy2(src, dest)
        print(f"Copied {src} to {dest}")
    except FileNotFoundError:
        print(f"File not found: {src}")

def delete_file(file):
    try:
        os.remove(file)
        print(f"Deleted {file}")
    except FileNotFoundError:
        print(f"File not found: {file}")

def create_file(file):
    with open(file, 'a') as f:
        print(f"Created {file}")

def list_files():
    files = os.listdir(current_directory)
    for file in files:
        print(file)

def search_files(keyword):
    try:
        result = subprocess.run(f'findstr /M /C:"{keyword}" *.*', shell=True, cwd=current_directory)
        if result.returncode == 0:
            print("Matching files:")
            print(result.stdout)
        else:
            print("No matching files found.")
    except FileNotFoundError:
        print("'findstr' command not found. This feature may not work on your system.")

def go_up():
    global current_directory
    current_directory = os.path.dirname(current_directory)
    os.chdir(current_directory)


def go_back():
    global current_directory
    parent_directory = os.path.dirname(current_directory)
    if parent_directory:
        os.chdir(parent_directory)
        current_directory = parent_directory
        print(f"Moved to parent directory: {current_directory}")
    else:
        print("Already at the root directory.")

class CommandCompleter(Completer):
    def get_completions(self, document, complete_event):
        word = document.get_word_before_cursor()
        if word:
            completions = []
            for cmd in available_commands:
                if cmd.startswith(word):
                    completions.append(Completion(cmd, start_position=-len(word)))
            return completions
        return []

available_commands = [
    "cd",
    "ls",
    "exit",
    "move",
    "copy",
    "delete",
    "create",
    "search",
    "up",
    "show",  
    "help",  
    "vi",
    "helpsys",
]


command_completer = CommandCompleter()


def show_help():
    print(f"{Fore.LIGHTYELLOW_EX}Available commands:{Fore.RESET}")
    print(f"{Fore.YELLOW}cd <directory>:{Fore.RESET} Change the current directory.")
    print(f"{Fore.YELLOW}ls:{Fore.RESET} List files in the current directory.")
    print(f"{Fore.YELLOW}exit:{Fore.RESET} Exit the shell.")
    print(f"{Fore.YELLOW}move <source> <destination>:{Fore.RESET} Move a file or directory.")
    print(f"{Fore.YELLOW}copy <source> <destination>:{Fore.RESET} Copy a file or directory.")
    print(f"{Fore.YELLOW}delete <file>:{Fore.RESET} Delete a file.")
    print(f"{Fore.YELLOW}create <file>:{Fore.RESET} Create a new file.")
    print(f"{Fore.YELLOW}vi:{Fore.RESET} simple file creator")
    print(f"{Fore.YELLOW}search <keyword>:{Fore.RESET} Search for files containing a keyword.")
    print(f"{Fore.YELLOW}up:{Fore.RESET} Navigate to the parent directory.")
    print(f"{Fore.YELLOW}show <directory>:{Fore.RESET} Show the contents of a directory.")
    print(f"{Fore.YELLOW}help:{Fore.RESET} Show this help message.")
    print(f"{Fore.YELLOW}helpsys:{Fore.RESET} Show system help message.")



while True:
    try:
        """user_input = prompt(
            ANSI(inp_pref()),
            completer=command_completer
        )"""
        user_input=input(inp_pref())

        if user_input == "":
            continue

        """history.append(user_input)"""

        """if user_input.lower() == "history":
            print("Command History:")
            for i, command in enumerate(history, start=1):
                print(f"{i}. {command}")
        el"""
        if user_input.startswith("cd "):
            directory = user_input[3:]
            try:
                os.chdir(directory)
                current_directory = os.getcwd()
                current_folder = current_directory.split("\\")[len(current_directory.split("\\"))-1] if current_directory.split("\\")[len(current_directory.split("\\"))-1]!="" else current_directory[:-2]
            except Exception as err:
                print(err)
        elif user_input.lower() == "ls":
            list_files()
        elif user_input.lower() == "exit":
            exit(0)
        elif user_input.startswith("move "):
            _, src, dest = user_input.split()
            move_file(src, dest)
        elif user_input.startswith("copy "):
            _, src, dest = user_input.split()
            copy_file(src, dest)
        elif user_input.startswith("delete "):
            _, file = user_input.split()
            delete_file(file)
        elif user_input.startswith("create "):
            _, file = user_input.split()
            create_file(file)
        elif user_input.startswith("vi"):
            con=""
            print(f"press {Fore.YELLOW}Ctrl+C{Fore.RESET} for confirm")
            try:
                while True:
                    con += input(Fore.LIGHTCYAN_EX)+"\n"
            except KeyboardInterrupt:
                file=input(f"{Fore.RESET}{Fore.YELLOW}What is the new file's name?{Fore.RESET} > ")
                with open(file, 'w') as f:
                    f.write(con)
                    print(f"{Fore.YELLOW}Created{Fore.RESET} {file}")
        elif user_input.startswith("search "):
            _, keyword = user_input.split()
            search_files(keyword)
        elif user_input.lower() == "up":
            go_up()
        elif user_input.lower() == "back":
            go_back()
        elif user_input.lower() == "help":
            show_help()
        elif user_input.lower() == "helpsys":
            os.system("help")
        elif user_input.lower().startswith("show "):
            directory = user_input[5:]
            show_directory_contents(directory)
        else:
            try:
                subprocess.run(user_input, shell=True, check=True)
            except subprocess.CalledProcessError:
                print(f"Command failed: {user_input}")

        """log_command(getuser(), user_input)"""
    except KeyboardInterrupt:
        print("^C")
