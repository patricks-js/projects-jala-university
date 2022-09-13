import time

import colorama
from colorama import Fore

colorama.init(autoreset=True)


def start_pomodoro(start: bool, time_production: int = 0, time_rest: int = 0):
    # * Case start == False so end process
    if not start:
        return print(f"{Fore.LIGHTBLUE_EX}End program!")

    # * End counts
    count_prod = 1
    count_rest = 1

    print(f"{Fore.CYAN}\nYour production time start now!!")
    time.sleep(0.6)
    # * Count the minutes (seconds for example) of the pomodoro
    while count_prod <= time_production:  # ! Minutes range of production time
        time.sleep(1)  # * 1 per minute (seconds)
        print(f"{count_prod}")
        count_prod += 1  # * decrease the counter

    time.sleep(1)

    if count_prod >= time_production:
        count_prod = 0
        print(f"{Fore.GREEN}\nYou have a {time_rest} minutes to rest! Enjoy!")
        time.sleep(0.6)
        # * Count the seconds of the pomodoro
        while count_rest <= time_rest:  # ! Minutes range of the rest time
            time.sleep(1)  # * 1 per minutes (seconds)
            print(count_rest)
            count_rest += 1  # * decrease the counter

        time.sleep(1)


def start_program():
    # * Start the program
    production_time = int(input("What the production time? "))
    rest_time = int(input("What the rest time? "))

    print(f"{Fore.MAGENTA}\nYour pomodoro has {production_time} minutes of the production and {rest_time} minutes of the rest for 4 times!\n")
    # ? The user wants to start the program
    lets_start = input(f"{Fore.BLUE}Want to start now? [y/n]: ")
    if lets_start == "y" or lets_start == "Y":
        count = 4  # ! How many times will the pomodoro spin
        while count >= 1:
            # * Run pomodoro
            start_pomodoro(True, production_time, rest_time)
            count -= 1
        print("Pomodoro finished")
    elif lets_start == "n" or lets_start == "N":
        # * End process
        start_pomodoro(False)
    else:
        # * Data validate
        print(f"{Fore.RED}\nInvalid responde! Try Again.\n")
        # * Restart process
        start_program()


start_program()
