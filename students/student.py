from scipy import stats

class Registration():
    def __init__(self):
        return None

    def register(self, student):
        return None



class Student():
    def __init__(self, name, id, grades):
        self.name = name
        self.id = id
        self.grades = grades
        self.weights = {}
        return None

    def grade_student(self, assignment, grade, weight):
        return self.grades.append({assignment:[grade, weight]})

    def class_standing(self, students=[]):
        percentiles = []
        for student in students:
            percentiles.append(student.class_grade())
        return stats.percentileofscore(percentiles, self.class_grade(), kind='rank')

    def class_grade(self):
        grades = {}
        lengths = {}
        to_return = 0
        for value in self.grades.values():
            if value[1] in grades.keys():
                grades[value[1]] += value[0]
                lengths[value[1]] += 1
            else:
                grades[value[1]] = value[0]
                lengths[value[1]] = 1
        for key in grades.keys():
            to_return += grades[key]/lengths[key]*key
        return to_return

    def get_id(self):
        return self.id