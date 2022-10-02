from colorama import Fore,Style, init


RED = Fore.RED
GREEN = Fore.GREEN
BLUE = Fore.BLUE
YELLOW = Fore.YELLOW
CYAN = Fore.CYAN
WHITE = Fore.WHITE
GRAY = Fore.WHITE
PURPLE = Fore.BLUE


STAR = ">"


def log(text=None, doInput=False, end=True, hidden=False):
    uwu = "UwUGen"
    space = " "

    trademark = f"{PURPLE}{Style.BRIGHT}{uwu}{STAR}"

    if text is None:
        print()
        return

    print(trademark,Style.RESET_ALL,text)