class Gradebook():
    def __init__(self):
        self.students = []

    def get_students(self):
        return self.students

    def add_student(self, student):
        self.students.append(student)
        return None

    def get_student(self, to_find):
        for student in self.students:
            if to_find == student.get_id():
                return student