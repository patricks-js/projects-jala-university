polygons = []

class Polygon:
    def __init__(self, side, number_of_side, apothem):
        self.side = side
        self.number_of_side = number_of_side
        self.apothem = apothem

    def calculate_perimeter(self):
        perimeter = self.side * self.number_of_side
        return print(f"The perimeter is {perimeter}")

    def calculate_area(self):
        perimeter = self.calculate_perimeter()
        area = (perimeter * self.apothem) / 2
        return print(f"The area is {area}")
            
def create_polygon():
    side = input("Side: ")
    number_of_side = input("Number of side: ")
    apothem = input("Apothem: ")
    polygon = Polygon(side, number_of_side, apothem)
    return polygon

# Tentei deixar a atividade um pouco mais elaborada, porém não consegui fazer tudo que eu queria, como mostrar as informações do poligono. A função de criar o polígono está funcionando bem e acrescentando o novo objeto ao array.

def show_polygon_information(polygon):
    print(polygon.calculate_perimeter())
    print(polygon.calculate_area())

def menu():
    menu_list = input("\nWhat do you want to do? \n1. Create Polygon\n2. Show Polygon information\n3. Exit\n")
    
    if (menu_list == "1"):
        polygons.append(create_polygon())
        menu()
    elif(menu_list == "2"):
        if(len(polygons) > 0):
            show_polygon_information(polygons[0]) # Não funciona 
        else: 
            print("No Polygons")
        menu()
    else: 
        print("Exit")

menu()