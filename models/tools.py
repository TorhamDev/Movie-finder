from rich import print
from os import system
from platform import platform


def print_banner() -> None:
    """
    printing the script banenr with python rich lib
    """

    banner = """
    [bold green]
    ███████████  ███                 █████    █████ ███████████ ███
    ░░███░░░░░░█ ░░░                 ░░███    ░░███ ░█░░░███░░░█░███
    ░███   █ ░  ████  ████████    ███████     ░███ ░   ░███  ░ ░███
    ░███████   ░░███ ░░███░░███  ███░░███     ░███     ░███    ░███
    ░███░░░█    ░███  ░███ ░███ ░███ ░███     ░███     ░███    ░███
    ░███  ░     ░███  ░███ ░███ ░███ ░███     ░███     ░███    ░░░ 
    █████       █████ ████ █████░░████████    █████    █████    ███
    ░░░░░       ░░░░░ ░░░░ ░░░░░  ░░░░░░░░    ░░░░░    ░░░░░    ░░░ 
                                                                    
                                                                    

    [/bold green]                                                                                                                            
    """
    print(banner)


def clear_terminal_screen() -> None:
    """
    clearing terminal by running clear in linux and mac. and cls in windows
    """

    runing_os = platform()

    if "Windows" in runing_os:
        system("cls")

    elif "Linux" in runing_os:
        system("clear")

    elif "macOS" in runing_os:
        system("clear")
