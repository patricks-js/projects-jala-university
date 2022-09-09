import reduce
import rs


class Student:
    def __init__(self, name, registration, class_student, notes):
        self.name = name
        self.registration = registration
        self.class_student = class_student
        self.notes = notes
        self.average = reduce.sum(notes) / len(notes)
        self.approved = True if self.average >= 7 else False

    def show_info(self):
        infos = f"\nName: {self.name}\nRegistration: {self.registration}\nClass: {self.class_student}\nNotes: {self.average}\nWas Approved: {self.approved}"

        return infos

    def student_approved(self):
        is_approved = f"The student {self.name} has been approved. Your average was {self.average}."
        is_reproved = f"The student {self.name} has not been approved. He needs at least 7 points to pass. Your average was {self.average}."

        return is_approved if self.approved else is_reproved


student1 = rs.register_student(Student, 4)

print(student1.show_info())
print(student1.student_approved())
