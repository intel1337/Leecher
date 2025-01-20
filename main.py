import os
import sys
import time
import colorama
from colorama import *

def main():
    def get_lines(filename):
        variable = 0
        with open(filename, "r") as fp:
            for line in fp:
                variable += 1
                print("Line Count:", variable)
        return variable

    def in_file(filename, substring, maxsize):
        j = 0
        with open(filename, "r") as fp:
            for line in fp:
                j += 1
                if substring in line:
                    print(f"{Fore.GREEN}[+] {Fore.WHITE}- Hit on line {j} : " + line.strip())
                if j == maxsize:
                    print("Max lines read.")
                    break

    print(f"""
____ ____ ____ ____ ____ ____ ____ 
||L |||e |||e |||c |||h |||e |||r ||
||__|||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|/__\|
          
[0] Exit        [1] DB lookup
[3] 
""")
    
    inp = input(f"{Fore.GREEN}leecher{Fore.CYAN}@{Fore.GREEN}root--{Fore.CYAN}$")

    if inp == "0":
        os.system('clear')
        sys.exit(0)
    if inp == "1":
        print(f"Search for Database Dir / file :")
        x = input(f"{Fore.GREEN}leecher{Fore.CYAN}@{Fore.GREEN}root--{Fore.CYAN}$")
        print(f"Search for a Name / Username / Email / IP / Phone Number / URL")
        v = input(f"{Fore.GREEN}leecher{Fore.CYAN}@{Fore.GREEN}root--{Fore.CYAN}$")
        line_count = get_lines(x)
        in_file(x, v, line_count)

if __name__ == "__main__":
    os.system('clear')
    main()
