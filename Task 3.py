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
        res_n = f'''СТУДЕНТЫ:
        Имя: {self.name}
        Фамилия: {self.surname}
        Средняя оценка за домашние задания: {self.average_mark_for_hw()}
        Курсы в процессе изучения: {", ".join(self.courses_in_progress)}
        Завершенные курсы: {", ".join(self.finished_courses)}'''
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
        res_n = f'''ЛЕКТОРЫ:
        Имя: {self.name}
        Фамилия: {self.surname}
        Средняя оценка за лекции: {self.average_mark_for_lectures()} '''
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
        res_n = f'''ПРОВЕРЯЮЩИЕ:
        Имя: {self.name}
        Фамилия: {self.surname}'''
        return res_n

some_reviewer = Reviewer('Some', 'Buddy')

some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python']

some_student = Student('Ruoy', 'Eman')
some_student.courses_in_progress += ['Python', 'Git']
some_student.finished_courses += ['Введение в программирование']

some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 9)
some_student.grades_lecturer(some_lecturer, 'Python', 10)
some_student.grades_lecturer(some_lecturer, 'Python', 9)
some_student.grades_lecturer(some_lecturer, 'Python', 9)

print(some_student)
print(some_lecturer)
print(some_reviewer)



print(f"Сравнение средней оценки лекторов и студентов: {some_lecturer.__lt__(some_student)}")