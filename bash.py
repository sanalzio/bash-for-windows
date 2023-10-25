from os import system, getlogin, getcwd, chdir, path
from colorama import Fore,init
from socket import gethostname
init()
while True:
  try:
    inp=input(Fore.LIGHTGREEN_EX+gethostname()+"@"+getlogin()+Fore.RESET+":"+Fore.BLUE+"~/"+getcwd().split("\\")[len(getcwd().split("\\"))-1]+Fore.RESET+"$ ")
    system(inp)
    if inp.startswith("cd"):
      dire=inp.replace("cd ", "").replace("'", "").replace('"', "")
      chdir(path.dirname(dire if dire.endswith("\\") or dire.endswith("/") else dire+"\\"))
    if inp.lower()=="exit":
      exit(0)
  except KeyboardInterrupt:
    inp=input("^C")
    system("^C"+inp)
    if inp.startswith("cd"):
      dire=inp.replace("cd ", "").replace("'", "").replace('"', "")
      chdir(path.dirname(dire if dire.endswith("\\") or dire.endswith("/") else dire+"\\"))