class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) \
                and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        some_student = f'Имя: {self.name}\n' \
                       f'Фамилия: {self.surname}\n' \
                       f'Средняя оценка за домашние задания: {self.av_rating()}\n' \
                       f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
                       f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return some_student

    def av_rating(self):
        sum_rating = 0
        len_rating = 0
        for course in self.grades.values():
            sum_rating += sum(course)
            len_rating += len(course)
        average_rating = round(sum_rating / len_rating, 2)
        return average_rating

    def av_rating_for_course(self, course):
        sum_rating = 0
        len_rating = 0
        for lesson in self.grades.keys():
            if lesson == course:
                sum_rating += sum(self.grades[course])
                len_rating += len(self.grades[course])
        average_rating = round(sum_rating / len_rating, 2)
        return average_rating

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Не сравнимо')
            return
        return self.av_rating() < other.av_rating()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        some_lecturer = f'Имя: {self.name}\n' \
                        f'Фамилия: {self.surname}\n' \
                        f'Средняя оценка за лекции: {self.av_rating()}'
        return some_lecturer

    def av_rating(self):
        sum_rating = 0
        len_rating = 0
        for course in self.grades.values():
            sum_rating += sum(course)
            len_rating += len(course)
        average_rating = round(sum_rating / len_rating, 2)
        return average_rating

    def av_rating_for_course(self, course):
        sum_rating = 0
        len_rating = 0
        for lesson in self.grades.keys():
            if lesson == course:
                sum_rating += sum(self.grades[course])
                len_rating += len(self.grades[course])
        average_rating = round(sum_rating / len_rating, 2)
        return average_rating

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Не сравнимо')
            return
        return self.av_rating() < other.av_rating()


class Reviewer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) \
                and course in self.courses_attached \
                and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        some_reviewer = f'Имя: {self.name}\n' \
                        f'Фамилия: {self.surname}'
        return some_reviewer


student = Student('Sherlok', 'Holms', 'M')
student.courses_in_progress += ['Python']
student.finished_courses += ['Введение в программирование']

student2 = Student('Stiw', 'Jons', 'F')
student2.courses_in_progress += ['Python']
student2.finished_courses += ['Java']

stud_lst = [student, student2]

lecturer = Lecturer('Peter', 'Parker')
lecturer.courses_attached += ['Python']

lecturer2 = Lecturer('Redg', 'Charlz')
lecturer2.courses_attached += ['Python']

lect_lst = [lecturer, lecturer2]

reviewer = Reviewer('Mon', 'Blue')
reviewer.courses_attached += ['Python']

reviewer2 = Reviewer('Lois', 'Lans')
reviewer2.courses_attached += ['Python']

reviewer.rate_hw(student, 'Python', 10)
reviewer.rate_hw(student, 'Python', 8)

reviewer2.rate_hw(student2, 'Python', 8)
reviewer2.rate_hw(student2, 'Python', 10)

student.rate_lecturer(lecturer, 'Python', 10)
student.rate_lecturer(lecturer, 'Python', 9)

student2.rate_lecturer(lecturer2, 'Python', 8)
student2.rate_lecturer(lecturer2, 'Python', 3)
def average_rating_for_course(course, list_):
    sum_rat = 0
    quant_rat = 0
    for stud in list_:
        for course in stud.grades:
            stud_sum_rating = stud.av_rating_for_course(course)
            sum_rat += stud_sum_rating
            quant_rat += 1
    average_rating = round(sum_rat / quant_rat, 2)
    return average_rating


 
print(f"Средняя оценка по курсу {''.join(student.courses_in_progress)} у студентов"
      f" {average_rating_for_course('Python', stud_lst)}")
print(f"Средняя оценка по курсу {''.join(lecturer.courses_attached)} у лекторов"
      f" {average_rating_for_course('Python', lect_lst)}"'\n')
print(reviewer.__str__(),'\n')
print(reviewer2.__str__(),'\n')
print(lecturer.__str__(),'\n')
print(lecturer2.__str__(),'\n')
print(student.__str__(),'\n')
print(student2.__str__(),'\n')
