# robots = []
# robots_name = []
import random

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


class PartRobot():
    def __init__(self, name: str, attack_level=0, defense_level=0, energy_consumption=0):
        self.name = name
        self.attack_level = attack_level
        self.defense_level = defense_level
        self.energy_consumption = energy_consumption
        self.available = True

    def get_status(self):
        return {
            print(self.name),
            print(" Attack level: ", self.attack_level),
            print(" Defense level: ", self.defense_level),
            print(" Energy consumption: ", self.energy_consumption),
            print(" Is available: ", self.available)
        }

    def reduce_defense(self, attack_level):
        self.defense_level = self.defense_level - attack_level
        if self.defense_level <= 0:
            self.defense_level = 0

    def is_available(self):
        return self.defense_level <= 0


class Robot:
    def __init__(self, name: str, color_code: str, player_name: str):
        self.name = name
        self.color_code = color_code
        self.player_name = player_name
        self.energy = 100
        self.alive = True
        self.parts = {
            "Head": PartRobot("Head", attack_level=5, defense_level=10, energy_consumption=5),
            "Left arm": PartRobot("Left arm", attack_level=3, defense_level=20, energy_consumption=10),
            "Right arm": PartRobot("Right arm", attack_level=6, defense_level=20, energy_consumption=10),
            "Left leg": PartRobot("Left leg", attack_level=4, defense_level=20, energy_consumption=15),
            "Right leg": PartRobot("Right leg", attack_level=8, defense_level=20, energy_consumption=15),
        }

    def say_hi(self):
        print(self.color_code)
        print(self.player_name, "Hello, my name is", self.name)

    def print_energy(self):
        print("We have", self.energy, " percent energy left")

    def print_parts(self):
        for part in self.parts.values():
            part.get_status()

    def attack(self, enemy_robot, part_to_use, part_to_attack):
        enemy_robot.parts[part_to_attack].defense_level -= self.parts[part_to_use].attack_level
        self.energy -= self.parts[part_to_use].energy_consumption

    def set_super(self):
        supers = [
            PartRobot("Armor", attack_level=0,
                      defense_level=30, energy_consumption=0),
            PartRobot("Lethal Weapon", attack_level=15,
                      defense_level=0, energy_consumption=10),
        ]
        super = random.choice(supers)
        self.parts["super"] = super
        print("You created me, so take this super part")
        super.print_status()

    def print_status(self):
        print(self.color_code)
        str_robot = robot_art.format(**self.get_part_status())
        self.greet()
        self.print_energy()
        print(str_robot)
        print(colors["White"])

    def get_part_status(self):
        part_status = {}
        for part in self.parts:
            status_dict = part.get_status_dict()
            part_status.update(status_dict)
        return part_status

    def is_there_available_part(self):
        for part in self.parts:
            if part.is_available():
                return True
        return False


robot1 = Robot("Megatron", colors["Cyan"], "Bill")
robot2 = Robot("Outobot", colors["Red"], "Fih do Bill")

print(robot2.print_parts())
print(robot1.attack(robot2, "Right arm", "Head"))
print(robot2.print_parts())
