__author__ = 'Sergey Khrul'

#
# Fifth task of Section #2
#
student1 = {"name": "Jones", "school": "Computing", "grades": (66, 77, 88)}
class_of_students = [
    {"name": "Jones", "school": "Computing", "grades": (66, 77, 88)},
    {"name": "Ken", "school": "Science", "grades": (56, 97, 28)},
    {"name": "Ken", "school": "Science", "grades": (4, 47, 21)}
]
"""Avarage grade count of student """
def average_grade (data):
    grades = data['grades']
    return sum(grades)/len(grades)

"""Avarage grade count of class """
def average_grade_all_student(student_list):
    total = 0
    count = len(student_list)
    for student in student_list:
        total += average_grade(student)
    return total/count

# Solution from video, but mine is better
# def average_grade_all_student2(student_list):
#     total = 0
#     count = 0
#     for student in student_list:
#         total += sum(student['grades'])
#         count += len(student['grades'])
#     return total/count




print(average_grade(student1))
print(average_grade_all_student(class_of_students))
# print(average_grade_all_student2(class_of_students))