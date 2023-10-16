# mrkr_module: Marker Module

    # Input: Takes in Application Ouput Console Display Text(string)

    # Output: Color-Coded Terminal Text In Console

    # Usage: Display Color-Coded Text In The Terminal To Convey Nuanced Importance/Meaning of The Displayed Messages

# Dependencies
    # Standard Module(s)
    # Installed Module(s)
import colorama
    # Local Module(s)

colorama.init() # Enable OS Virtual Terminal

###### ###### ###### ###### ######
###### Interface For mrkr   ######
###### ###### ###### ###### ######

# print green terminal text
def Green(text: str) -> None:
    print(colorama.Fore.LIGHTGREEN_EX, text, colorama.Style.RESET_ALL)

# print cyan terminal text
def Cyan(text: str) -> None:
    print(colorama.Fore.LIGHTCYAN_EX, text, colorama.Style.RESET_ALL)

# print yellow terminal text
def Yellow(text: str) -> None:
    print(colorama.Fore.LIGHTYELLOW_EX, text, colorama.Style.RESET_ALL)

# print magenta terminal text
def Magenta(text: str) -> None:
    print(colorama.Fore.LIGHTMAGENTA_EX, text, colorama.Style.RESET_ALL)
    
# print red terminal text
def Red(text: str) -> None:
    print(colorama.Fore.LIGHTRED_EX, text, colorama.Style.RESET_ALL)