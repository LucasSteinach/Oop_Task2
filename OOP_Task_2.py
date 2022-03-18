class Student:
    def __init__(self, name, surname, gender, list_of_std):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grade = 0
        list_of_std += [self]

    def grade_lecturer(self, lector, course, grade):
        if (isinstance(lector, Lecturer) and course in self.courses_in_progress
                and course in lector.courses_attached and 0 < grade < 11):
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
            sum_of_grades = 0
            count_of_grades = 0
            for list_of_grades in lector.grades.values():
                sum_of_grades += sum(list_of_grades)
                count_of_grades += len(list_of_grades)
            lector.average_grade = round(sum_of_grades / count_of_grades, 2)
        else:
            return 'ERROR'


    def __str__(self):
        return f"""Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {self.average_grade}
Курсы в процессе изучения: {', '.join(self.courses_in_progress)}
Завершенные курсы: {', '.join(self.finished_courses)}
"""

    def __lt__(self, other):
        if not isinstance(other, Student):
            return
        else:
            return self.average_grade < other.average_grade


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname, list_of_lectors):
        super().__init__(name, surname)
        self.grades = {}
        self.average_grade = 0
        list_of_lectors += [self]

    def __str__(self):
        return f"""Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {self.average_grade}
"""

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return
        else:
            return self.average_grade < other.average_grade

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
            sum_of_grades = 0
            count_of_grades = 0
            for each_subject in student.grades.values():
                sum_of_grades += sum(each_subject)
                count_of_grades += len(each_subject)
            student.average_grade = round(sum_of_grades / count_of_grades, 2)
        else:
            return 'Ошибка'

    def __str__(self):
        return f"""Имя: {self.name}
Фамилия: {self.surname}
"""


def avg_grade_hw(list_of_students, course):
    sum_of_grades = 0
    count_of_grades = 0
    for student in list_of_students:
        if not isinstance(student, Student):
            return 'Wrong type of object(not Student)'
        elif course not in student.grades:
            continue
        else:
            sum_of_grades += sum(student.grades[course])
            count_of_grades += len(student.grades[course])
    if count_of_grades == 0:
        return 'This course is not rated yet'
    else:
        return f'Средняя оценка по предмету "{course}" равна {sum_of_grades / count_of_grades: .2f}'


def avg_lecturers_grade(list_of_lectors, course):
    sum_of_grades = 0
    count_of_grades = 0
    for lector in list_of_lectors:
        if not isinstance(lector, Lecturer):
            return 'Wrong type of object(not Lecturer)'
        elif course not in lector.grades:
            continue
        else:
            sum_of_grades += sum(lector.grades[course])
            count_of_grades += len(lector.grades[course])
    if count_of_grades == 0:
        return 'This course is not rated yet'
    else:
        return f'Средняя оценка за лекции по предмету "{course}" равна {sum_of_grades / count_of_grades: .2f}'


list_of_students = []
list_of_lecturers = []

student1 = Student('Ruoy', 'Eman', 'your_gender', list_of_students)
student1.courses_in_progress += ['Python', 'Full-Stack Developer']
student1.finished_courses += ['Введение в профессию']
student2 = Student('Siegfried', 'Colman', 'his_gender', list_of_students)
student2.courses_in_progress += ['Python', 'Введение в профессию']

reviewer1 = Reviewer('Some', 'Buddy')
reviewer2 = Reviewer('Awesome', 'Body')
reviewer1.courses_attached += ['Python', 'Введение в профессию']
reviewer2.courses_attached += ['Python', 'Full-Stack Developer']

lecturer1 = Lecturer('Hector', 'Shmector', list_of_lecturers)
lecturer1.courses_attached += ['Python', 'Full-Stack Developer']
lecturer2 = Lecturer('Cheetos', 'Cheeters', list_of_lecturers)
lecturer2.courses_attached += ['Python', 'Full-Stack Developer', 'Введение в профессию']

reviewer1.rate_hw(student1, 'Python', 10)
reviewer2.rate_hw(student1, 'Python', 9)
reviewer2.rate_hw(student1, 'Введение в профессию', 10)     # не добавится, т.к. у ревьюера2 нет такого предмета
reviewer1.rate_hw(student1, 'Full-Stack Developer', 8)      # не добавится, т.к. у ревьюера2 нет такого предмета
reviewer1.rate_hw(student2, 'Python', 6)
reviewer2.rate_hw(student2, 'Python', 5)
reviewer2.rate_hw(student2, 'Введение в профессию', 7)
reviewer1.rate_hw(student2, 'Full-Stack Developer', 9)

student2.grade_lecturer(lecturer2, 'Python', 8)
student2.grade_lecturer(lecturer1, 'Введение в профессию', 8)   # у лектор1 нет такого предмета
student2.grade_lecturer(lecturer2, 'Python', 6)
student1.grade_lecturer(lecturer1, 'Full-Stack Developer', 8)
student1.grade_lecturer(lecturer1, 'Python', 10)
student2.grade_lecturer(lecturer2, 'Введение в профессию', 8)

print(student1)
print(student2)
print(student1 < student2)
print(student1 > student2, '\n')
print(reviewer1)
print(reviewer2)
print(lecturer1)
print(lecturer2)
print(lecturer1 < lecturer2)
print(lecturer1 > lecturer2)
print(avg_grade_hw(list_of_students, 'Python'))
print(avg_lecturers_grade(list_of_lecturers, 'Python'))

