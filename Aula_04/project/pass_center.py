import colorama
from colorama import Fore

colorama.init(autoreset=True)

passwords: dict = {}


class NewPassword:
    def __init__(self, origin: str, password: str):
        self.origin = origin
        self.password = password


class PasswordCenter:
    def __init__(self, master: str, pin: int):
        self.master = master
        self.pin = pin

    def register_password(self):
        print(f"{Fore.BLUE}\n========== Register new password ==========")

        origin = input("\nPassword origin: ")
        password = input("Password: ")

        new_pass = NewPassword(origin.capitalize(), password)
        passwords.update({f"{new_pass.origin}": f"{new_pass.password}"})

        print(f"{Fore.GREEN}\nPassword registered successfully")

    def see_keys(self):
        print(f"{Fore.BLUE}\n========== See keys ==========")

        pin = int(input("\nEnter your pin: "))
        if pin == self.pin:
            keys = []
            i = 1
            for key in passwords.keys():
                keys.append(f"{i}° key: {key}")
                i += 1
            print(f"{Fore.CYAN}Your keys: {keys}")

        else:
            print(f"{Fore.RED}Pin don't match! Try again.")
            self.see_keys()

    def see_password(self):
        print(f"{Fore.BLUE}\n========== See Password ==========")

        pin = int(input("\nEnter your pin: "))
        if pin == self.pin:
            password = input("Which password you want see: ").capitalize()
            if password in passwords.keys():
                print(
                    f"{Fore.CYAN}Password by {password}: {passwords.get(password)}"
                )

            else:
                print(f"{Fore.RED}Incorrect key! Try again!")
                self.see_password()

        else:
            print(f"{Fore.RED}Pin don't match! Try again.")
            self.see_password()


def register_user():
    print(f"{Fore.BLUE}========== Register new user ==========")

    master = input("Enter your name: ")
    pin = int(input("\n(Security) Enter your pin: (min: 4 numbers) "))

    pin_digits = len(str(pin))
    if pin_digits < 4:
        print(f"{Fore.RED}\nError! Min digits is 4(four)")
        register_user()
        return

    print(f"{Fore.GREEN}\nUser registered successfully")
    int(pin)

    new_user = PasswordCenter(master, pin)
    return new_user


patrick = register_user()

patrick.register_password()
patrick.register_password()
patrick.register_password()
patrick.see_keys()
patrick.see_password()
