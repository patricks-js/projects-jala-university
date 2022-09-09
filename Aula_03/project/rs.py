def register_student(obj, quantity_notes):
    name = input("Enter student name: ")
    registration = int(input("Enter student registration: "))
    class_student = input("Enter student class: ")
    notes = []
    count = 1
    while 0 < quantity_notes:
        notes.append(float(input(f"Enter with the {count}° note: ")))
        count += 1
        quantity_notes -= 1

    student = obj(name, registration, class_student, notes)
    return student
