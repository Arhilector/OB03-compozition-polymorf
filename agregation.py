class Teacher():
    def teach(self):
        print("Учитель преподаёт")

class School():
    def __init__(self, new_teacher):
        self.teacher = new_teacher


    def start_lesson(self):
        self.teacher.teach()

vova = Teacher()
my_school = School(vova)

my_school.start_lesson()