gradebook = {}

def add_student(student):
   gradebook[student] = []

def add_grade(student, grade):
    try:
        gradebook[student].append(grade)
    except KeyError:
        return f"'{student}' not enrolled"

def get_grade(student):
   return gradebook.get(student)

def grade_average(grade):
    return float(sum(grade) / len(grade))

def class_average(student_grades):
    all_grades = []
    for grades in student_grades:
        all_grades.append(grade_average(grades))
    return grade_average(all_grades)


def letter_grade(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"
        


