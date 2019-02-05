from students import student
from gradebook import grader

grades = {1:[1,0.8], 2:[0.8, 0.2], 3:[0.9, 0.8]}

roster = grader.Gradebook()
roster.add_student(student.Student('blake', 1, grades))
roster.get_students()
s = roster.get_student(1)


print(s.class_standing(roster.get_students()))