from programs import *
from programs import __all__
from programs import pkgm
from programs import tutr
from programs import execute
from programs import animate
from programs import clear
from programs import version
from programs import echo
from programs import programmanager
from programs import ls
from colorama import Fore, Back
import os


def check(cmd):
    if cmd.lower().startswith("dir") or cmd.lower().startswith("ls"):
        ls.listdirectory(cmd[3:])
    elif cmd.lower().startswith("./"):
        programmanager.run(cmd[2:])
    elif cmd.lower().startswith("echo "):
        echo.echo(cmd)
    elif cmd.lower().startswith("help"):
        help.help()
    elif cmd.lower().startswith("version"):
        version.version()
    elif cmd.lower().startswith("clear") or cmd.lower().startswith("cls"):
        clear.clearConsole()
    elif cmd.lower().startswith("animate "):
        animate.animate(cmd)
    elif cmd.lower().startswith("exit"):
        exit.rl()
    elif cmd.lower().startswith("pkgm downloadrepo"):
        pkgm.downloadrepo()
    elif cmd.lower().startswith("pkgm install "):
        pkgm.install(cmd.split(' ')[2])
    elif cmd.lower().startswith("tutr "):
        tutr.tutr(cmd)
    elif cmd.lower().startswith("exec "):
        execute.exec(cmd)
    elif cmd.lower().startswith("pkgm list"):
        pkgm.list()
    elif cmd.lower().startswith("pkgm run"):
        pkgm.run(cmd)
    else:
        print("Command not found run help for list of commands")
