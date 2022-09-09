robots = []
robots_name = []


class PartRobot():
    def __init__(self, name: str, attack_level=0, defense_level=0, energy_consumption=0):
        self.name = name
        self.attack_level = attack_level
        self.defense_level = defense_level
        self.energy_consumption = energy_consumption

    def get_status_dict(self):
        formatted_name = self.name.replace(" ", "_").lower()
        return {
            f"{formatted_name}_name": self.name.upper(),
            f"{formatted_name}_status": self.is_available(),
            f"{formatted_name}_attack": self.attack_level,
            f"{formatted_name}_defense": self.defense_level,
            f"{formatted_name}_energy_consume": self.energy_consumption,
        }

    def reduce_defense(self, attack_level):
        self.defense_level = self.defense_level - attack_level
        if self.defense_level <= 0:
            self.defense_level = 0

    def is_available(self):
        return self.defense_level <= 0


class Robot:
    def __init__(self, name: str, color_code: str):
        self.name = name
        self.color_code = f"#{color_code}"
        self.energy = 100
        self.parts = [
            PartRobot("Head", attack_level=5,
                      defense_level=10, energy_consumption=5),
            PartRobot("Weapon", attack_level=15,
                      defense_level=0, energy_consumption=10),
            PartRobot("Left Arm", attack_level=3,
                      defense_level=20, energy_consumption=10),
            PartRobot("Right Arm", attack_level=6,
                      defense_level=20, energy_consumption=10),
            PartRobot("Left Leg", attack_level=4,
                      defense_level=20, energy_consumption=15),
            PartRobot("Right Leg", attack_level=8,
                      defense_level=20, energy_consumption=15),
        ]

    def greet(self):
        print("Hello, my name is", self.name)

    def print_energy(self):
        print("We have", self.energy, " percent energy left")


def createRobot(code_robot):
    name: str = input(f"Enter the name of the robot {code_robot}: \n    ")
    color_code: str = input("\nEnter the color code of the robot: \n    ")
    robot = Robot(name, color_code)
    robots.append(robot)
    robots_name.append(robot.name)

    new_robot: str = input("\nWant to add a new robot? [y/n] \n    ")

    if (new_robot == "y"):
        createRobot(len(robots) + 1)
    else:
        print(f"Your robot list: {robots_name}")


createRobot(len(robots) + 1)
