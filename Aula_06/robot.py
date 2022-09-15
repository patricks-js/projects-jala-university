import random

from colorama import Fore
from typing_extensions import Self

robot_art = r"""
        0: {head_name}
        Is available: {head_status}
        Attack: {head_attack}
        Defense: {head_defense}
        Energy consumption: {head_energy_consump}
              ^
              |                   |1: {weapon_name}
              |                   |Is available: {weapon_status}
     ____     |    ____           |Attack: {weapon_attack}
    |oooo|        |oooo|  ------> |Defense: {weapon_defense}
    |oooo| .----. |oooo|          |Energy consumption: {weapon_energy_consump}
    |Oooo|/\_||_/\|oooO|              
    `----' / __ \ `----'             |2: {left_arm_name}
    ,/ |#|/\/__\/\|#| \,             |Is available: {left_arm_status}
   /  \|#|| |/\| ||#|/  \            |Attack: {left_arm_attack}
  / \_/|_|| |/\| ||_|\_/ \           |Defense: {left_arm_defense}
 |_\/    o\=----=/o    \/_|          |Energy consumption: {left_arm_energy_consump}
 <_>      |=\__/=|      <_>  ------> | 
 <_>      |------|      <_>          |3: {right_arm_name}
 | |   ___|======|___   | |          |Is available: {right_arm_status}
//\\  / |O|======|O| \  //\\         |Attack: {right_arm_attack}
|  |  | |O+------+O| |  |  |         |Defense: {right_arm_defense}
|\/|  \_+/        \+_/  |\/|         |Energy consumption: {right_arm_energy_consump}
\__/  _|||        |||_  \__/ 
      | ||        || |          |4: {left_leg_name}
     [==|]        [|==]         |Is available: {left_leg_status}
     [===]        [===]         |Attack: {left_leg_attack}
      >_<          >_<          |Defense: {left_leg_defense}
     || ||        || ||         |Energy consumption: {left_leg_energy_consump}
     || ||        || || ------> |
     || ||        || ||         |5: {right_leg_name}
   __|\_/|__    __|\_/|__       |Is available: {right_leg_status}
  /___n_n___\  /___n_n___\      |Attack: {right_leg_attack}
                                |Defense: {right_leg_defense}
                                |Energy consumption: {right_leg_energy_consump}
"""

colors = {
    "Black": '\x1b[90m',
    "Blue": '\x1b[94m',
    "Cyan": '\x1b[96m',
    "Green": '\x1b[92m',
    "Magenta": '\x1b[95m',
    "Red": '\x1b[91m',
    "White": '\x1b[97m',
    "Yellow": '\x1b[93m',
}


class Part:
    def __init__(self, name: str, attack_level=0, defense_level=0, energy_consumption=0):
        self.name = name
        self.attack_level = attack_level
        self.defense_level = defense_level
        self.energy_consumption = energy_consumption

    def get_status_dict(self):
        formatted_name = self.name.replace(" ", "_").lower()
        return {
            f"{formatted_name}_name": self.name.capitalize().strip(),
            f"{formatted_name}_status": self.is_available(),
            f"{formatted_name}_attack": self.attack_level,
            f"{formatted_name}_defense": self.defense_level,
            f"{formatted_name}_energy_consump": self.energy_consumption,
        }

    def reduce_defense(self, attack_level):
        self.defense_level = self.defense_level - attack_level
        if self.defense_level <= 0:
            self.defense_level = 0

    def is_available(self):
        return True if self.defense_level > 0 else False

    def print_status(self):
        print(self.name)
        print(" Attack level: ", self.attack_level)
        print(" Defense level: ", self.defense_level)
        print(" Energy consumption: ", self.energy_consumption)
        print(" Is available: ", self.is_available())


class Robot:
    def __init__(self, name, color_code, player_name):
        self.name = name
        self.color_code = color_code
        self.player_name = player_name
        self.energy = 100
        self.vivo = True
        self.parts = {
            "Head": Part("Head", attack_level=5, defense_level=10, energy_consumption=5),
            "Weapon": Part("Weapon", attack_level=15, defense_level=0, energy_consumption=10),
            "Left arm": Part("Left arm", attack_level=3, defense_level=20, energy_consumption=10),
            "Right arm": Part("Right arm", attack_level=6, defense_level=20, energy_consumption=10),
            "Left leg": Part("Left leg", attack_level=4, defense_level=20, energy_consumption=15),
            "Right leg": Part("Right leg", attack_level=8, defense_level=20, energy_consumption=15),
        }

    def say_hi(self):
        print(self.color_code)
        print(self.player_name, "Hello, my name is", self.name)

    def print_energy(self):
        print("We have", self.energy, " percent energy left")
        print("\n")

    def is_on(self):
        return self.energy >= 0

    def print_status(self, attacked_part):
        dict_part = self.parts.get(attacked_part).get_status_dict()
        print(f"{Fore.BLUE}\nStatus: ", Fore.RESET)
        for k, v in dict_part.items():
            print(f"\n{k}: {v}")
        print("\n")

    def get_part_status(self):
        part_status = {}
        for part in self.parts.values():
            status_dict = part.get_status_dict()
            part_status.update(status_dict)
        return part_status

    def print_status_art(self):
        print(self.color_code)
        str_robot = robot_art.format(**self.get_part_status())
        self.say_hi()
        self.print_energy()
        print(str_robot)
        print(colors["White"])

    def attack(self, enemy_robot: Self, part_to_use: str, part_to_attack: str):
        enemy_robot.parts[part_to_attack].defense_level -= self.parts[part_to_use].attack_level
        self.energy -= self.parts[part_to_attack].energy_consumption

    def is_there_available_part(self):
        for part in self.parts.values():
            return True if part.is_available() else False


def build_robot():
    robot_name = input("Robot name: ").strip()
    player_name = input("Player name: ").strip()
    color_code = choose_color()
    robot = Robot(robot_name, color_code, player_name)
    return robot


def choose_color():
    available_colors = colors
    print("Available colors:")
    for key, value in available_colors.items():
        print(value, key)
    print(colors["White"])
    chosen_color = input("Choose a color: ").strip()
    color_code = available_colors[chosen_color]
    return color_code


def create_players():
    print(f"{Fore.GREEN}Welcome to the game!\n")
    print(f"Datas for player 1:\n{Fore.RESET}")
    r1 = build_robot()
    r1.print_status_art()
    print(f"{Fore.GREEN}Datas for player 2:\n{Fore.RESET}")
    r2 = build_robot()
    r2.print_status_art()
    return r1, r2


def attack_enemy(my_robot: Robot, enemy: Robot):
    print(f"{Fore.RED}Your round {my_robot.name}{Fore.RESET}")

    my_robot.print_status_art()

    print("What part name should I use to attack?:")
    part_to_use = input("Choose a part: ").strip()

    print(f"\nWhich name part of the {enemy.name} should we attack?")
    part_to_attack = input("Choose a enemy part to attack: ").strip()

    my_robot.attack(enemy, part_to_use, part_to_attack)

    enemy.print_status(part_to_attack)


def play():
    playing = True  # ?

    robot_one, robot_two = create_players()

    current_robot = robot_one
    enemy_robot = robot_two
    round = 0

    while playing:
        if round % 2 == 0:
            current_robot = robot_one
            enemy_robot = robot_two
        else:
            current_robot = robot_two
            enemy_robot = robot_one

        attack_enemy(current_robot, enemy_robot)

        round += 1

        enemy_parts_is_available = enemy_robot.is_there_available_part()

        if not (enemy_robot.is_on() or enemy_parts_is_available):
            playing = False
            print(f"{Fore.GREEN}\nCongratulations {current_robot.name}, you win!")


play()
