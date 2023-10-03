# Dependencies
    # Standard Lib(s)
    # Installed Lib(s)
import colorama
    # Local Module(s)

colorama.init() # Enable OS Virtual Terminal

###### ###### ###### ###### ######
###### Interface For mrkr   ######
###### ###### ###### ###### ######

# Color Terminal Text Helper Class
class mrkr:

    # print green terminal text
    @staticmethod
    def Green(text: str) -> None:
        print(colorama.Fore.LIGHTGREEN_EX, text, colorama.Style.RESET_ALL)

    # print cyan terminal text
    @staticmethod
    def Cyan(text: str) -> None:
        print(colorama.Fore.LIGHTCYAN_EX, text, colorama.Style.RESET_ALL)

    # print yellow terminal text
    @staticmethod
    def Yellow(text: str) -> None:
        print(colorama.Fore.LIGHTYELLOW_EX, text, colorama.Style.RESET_ALL)

    # print magenta terminal text
    @staticmethod
    def Magenta(text: str) -> None:
        print(colorama.Fore.LIGHTMAGENTA_EX, text, colorama.Style.RESET_ALL)

    # print red terminal text
    @staticmethod
    def Red(text: str) -> None:
        print(colorama.Fore.LIGHTRED_EX, text, colorama.Style.RESET_ALL)