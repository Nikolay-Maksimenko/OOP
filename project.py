class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached and 1 <= grade <= 10:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def get_av_grade(self):
        sum_of_grades = 0
        number_of_grades = 0
        for list_of_grades in self.grades.values():
            for grade in list_of_grades:
                sum_of_grades += grade
                number_of_grades += 1
        if number_of_grades != 0:
            average_grade = sum_of_grades / number_of_grades
            return average_grade

    def __str__(self):
        output = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.get_av_grade()} \nКурсы в процессе изучения: {self.courses_in_progress} \nЗавершенные курсы: {self.finished_courses}'
        return output

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Не студент')
            return
        return self.get_av_grade() < other.get_av_grade()

    def __gt__(self, other):
        if not isinstance(other, Student):
            print('Не студент')
            return
        return self.get_av_grade() > other.get_av_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            print('Не студент')
            return
        return self.get_av_grade() == other.get_av_grade()

    def __ne__(self, other):
        if not isinstance(other, Student):
            print('Не студент')
            return
        return self.get_av_grade() != other.get_av_grade()

    def __le__(self, other):
        if not isinstance(other, Student):
            print('Не студент')
            return
        return self.get_av_grade() <= other.get_av_grade()

    def __ge__(self, other):
        if not isinstance(other, Student):
            print('Не студент')
            return
        return self.get_av_grade() >= other.get_av_grade()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def get_av_grade(self):
        sum_of_grades = 0
        number_of_grades = 0
        for list_of_grades in self.grades.values():
            for grade in list_of_grades:
                sum_of_grades += grade
                number_of_grades += 1
        if number_of_grades != 0:
            average_grade = sum_of_grades / number_of_grades
            return  average_grade

    def __str__(self):
        output = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.get_av_grade()}'
        return output

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Не лектор')
            return
        return self.get_av_grade() < other.get_av_grade()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            print('Не лектор')
            return
        return self.get_av_grade() > other.get_av_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            print('Не лектор')
            return
        return self.get_av_grade() == other.get_av_grade()

    def __ne__(self, other):
        if not isinstance(other, Lecturer):
            print('Не лектор')
            return
        return self.get_av_grade() != other.get_av_grade()

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            print('Не лектор')
            return
        return self.get_av_grade() <= other.get_av_grade()

    def __ge__(self, other):
        if not isinstance(other, Lecturer):
            print('Не лектор')
            return
        return self.get_av_grade() >= other.get_av_grade()

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress and 1 <= grade <= 10:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        output = f'Имя: {self.name} \nФамилия: {self.surname}'
        return output

def get_av_grade_student(students, course):
    for student in students:
        sum_of_grades = 0
        number_of_grades = 0
        av_grade = 0
        if isinstance(student, Student) and course in student.courses_in_progress:
            for grade in student.grades[course]:
                sum_of_grades += grade
                number_of_grades += 1
            if number_of_grades != 0:
                av_grade = sum_of_grades / number_of_grades
        if av_grade != 0:
            print(f'Средняя оценка студента {student.name} {student.surname} по курсу {course} = {av_grade}')


def get_av_grade_lecturer(lecturers, course):
    for lecturer in lecturers:
        sum_of_grades = 0
        number_of_grades = 0
        av_grade = 0
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            for grade in lecturer.grades[course]:
                sum_of_grades += grade
                number_of_grades += 1
            if number_of_grades != 0:
                av_grade = sum_of_grades / number_of_grades
        if av_grade != 0:
            print(f'Средняя оценка лектора {lecturer.name} {lecturer.surname} по курсу {course} = {av_grade}')

nikolay = Student('Николай', 'Максименко', 'м')
maksim = Student('Максим', 'Петров', 'м')
ivan = Lecturer('Иван', 'Новиков')
dmitriy = Lecturer('Дмитрий', 'Смирнов')
aleksandr = Reviewer('Александр', 'Смирнов')
vladimir = Reviewer('Владимир', 'Иванов')

nikolay.courses_in_progress.append('Python')
nikolay.courses_in_progress.append('SQL')
nikolay.add_courses('Pascal')
maksim.courses_in_progress.append('Python')
maksim.courses_in_progress.append('C++')
maksim.add_courses('Delphi')
ivan.courses_attached.append('Python')
ivan.courses_attached.append('SQL')
dmitriy.courses_attached.append('Python')
dmitriy.courses_attached.append('C++')
aleksandr.courses_attached.append('Python')
aleksandr.courses_attached.append('C++')
vladimir.courses_attached.append('Python')
vladimir.courses_attached.append('SQL')

nikolay.rate_lecturer(ivan, 'Python', 7)
nikolay.rate_lecturer(ivan, 'SQL', 8)
nikolay.rate_lecturer(dmitriy, 'Python', 9)

maksim.rate_lecturer(ivan, 'Python', 4)
maksim.rate_lecturer(dmitriy, 'C++', 9)
maksim.rate_lecturer(dmitriy, 'Python', 7)

aleksandr.rate_hw(nikolay, 'Python', 7)
aleksandr.rate_hw(maksim, 'Python', 5)
aleksandr.rate_hw(maksim, 'C++', 4)

vladimir.rate_hw(nikolay, 'Python', 8)
vladimir.rate_hw(maksim, 'Python', 7)
vladimir.rate_hw(nikolay, 'SQL', 9)

print(maksim)
print()
print(nikolay)
print()
print(ivan)
print()
print(dmitriy)
print()
print(aleksandr)
print()
print(vladimir)
print()
print(nikolay < maksim)
print(nikolay > maksim)
print(nikolay == maksim)
print(nikolay != maksim)
print(nikolay <= maksim)
print(nikolay >= maksim)
print()
print(ivan < dmitriy)
print(ivan > dmitriy)
print(ivan == dmitriy)
print(ivan != dmitriy)
print(ivan <= dmitriy)
print(ivan >= dmitriy)
print()
list_of_student = [nikolay, maksim]
get_av_grade_student(list_of_student, 'Python')
print()
list_of_lecturer= [ivan, dmitriy]
get_av_grade_lecturer(list_of_lecturer, 'Python')