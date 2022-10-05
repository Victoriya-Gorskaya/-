class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_in_progress = []
        self.finished_courses = []
        self.grades = {}

    def grades_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades_for_lectures:
                lecturer.grades_for_lectures[course] += [grade]
            else:
                lecturer.grades_for_lectures[course] = [grade]
        else:
            return 'Ошибка'

    def average_mark_for_hw(self):        
         mark_hw = round(sum(map(sum, self.grades.values())) / sum(map(len, self.grades.values())), 1)
         return mark_hw

    def __str__(self):
        res_n = f'''
        Имя: {self.name}
        Фамилия: {self.surname}
        Средняя оценка за домашние задания: {self.average_mark_for_hw()}
        Курсы в процессе изучения: {", ".join(self.courses_in_progress)}
        Завершенные курсы: {", ".join(self.finished_courses)}
        '''
        return res_n
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
                
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades_for_lectures = {}

    def average_mark_for_lectures(self):        
        av_mark = round(sum(map(sum, self.grades_for_lectures.values())) / sum(map(len, self.grades_for_lectures.values())), 1)
        return av_mark

    def __lt__(self, student):
        if not isinstance (student, Student):
            print('Этот человек не студент')
            return
        return self.average_mark_for_lectures() < student.average_mark_for_hw()

    def __str__(self):
        res_n = f'''
        Имя: {self.name}
        Фамилия: {self.surname}
        Средняя оценка за лекции: {self.average_mark_for_lectures()} 
        '''
        return res_n


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        res_n = f'''
        Имя: {self.name}
        Фамилия: {self.surname}
        '''
        return res_n

some_reviewer1 = Reviewer('Petr', 'Petrov')
some_reviewer2 = Reviewer('Ivan', 'Ivanov')

some_lecturer1 = Lecturer('Nikolay', 'Nikolaev')
some_lecturer2 = Lecturer('Some', 'Buddy')
some_lecturer1.courses_attached += ['Python', 'Git']
some_lecturer2.courses_attached += ['Python', 'Git']

some_student1 = Student('Ruoy', 'Eman')
some_student2 = Student('Irina', 'Grey')

some_student1.courses_in_progress += ['Python', 'Git']
some_student2.courses_in_progress += ['Python','Git']
some_student1.finished_courses += ['Введение в программирование']
some_student2.finished_courses += ['Введение в программирование']

some_reviewer1.rate_hw(some_student1, 'Python', 10)
some_reviewer1.rate_hw(some_student1, 'Git', 10)
some_reviewer1.rate_hw(some_student2, 'Python', 9)
some_reviewer1.rate_hw(some_student2, 'Git', 10)

some_reviewer2.rate_hw(some_student1, 'Python', 10)
some_reviewer2.rate_hw(some_student1, 'Git', 10)
some_reviewer2.rate_hw(some_student2, 'Python', 9)
some_reviewer2.rate_hw(some_student2, 'Git', 9)

some_student1.grades_lecturer(some_lecturer1, 'Python', 10)
some_student1.grades_lecturer(some_lecturer1, 'Git', 9)
some_student1.grades_lecturer(some_lecturer2, 'Python', 10)
some_student1.grades_lecturer(some_lecturer2, 'Git', 9)

some_student2.grades_lecturer(some_lecturer1, 'Python', 9)
some_student2.grades_lecturer(some_lecturer1, 'Git', 10)
some_student2.grades_lecturer(some_lecturer2, 'Python', 10)
some_student2.grades_lecturer(some_lecturer2, 'Git', 10)

print(f'Студенты: {some_student1} {some_student2}')
print(f'Лекторы: {some_lecturer1} {some_lecturer2}')
print(f'Проверяющие: {some_reviewer1} {some_reviewer2}')

students = [some_student1, some_student2]

def av_mark_for_course(students, courses):
    sum_marks = 0
    amount = 0
    for student in students:
        for mark in student.grades[courses]:
            sum_marks += mark
            amount += 1
    return round(sum_marks/amount, 1)
 

lecturers = [some_lecturer1, some_lecturer2]
def av_mark_for_lect(lecturers, courses):
    sum_marks = 0
    amount = 0
    for lecturer in lecturers:
        for mark in lecturer.grades_for_lectures[courses]:
            sum_marks += mark
            amount += 1
    return round(sum_marks/amount, 1)

print(f"Средняя оценка за ДЗ по Python: {av_mark_for_course(students, 'Python')}")
print(f"Средняя оценка за ДЗ по Git: {av_mark_for_course(students, 'Git')}")

print(f"Средняя оценка за лекции по Python: {av_mark_for_lect(lecturers, 'Python')}")
print(f"Средняя оценка за лекции по Git: {av_mark_for_lect(lecturers, 'Git')}")
