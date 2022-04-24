class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.teaching_the_course:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average(self, students, course, average_grades):
        for student in students:
            if isinstance(student, Student) and course in student.grades[course]:
                average_grades.extend(student.grades[course])
            return

    def __str__(self):
        return f" \nИмя: {self.name}" \
               f" \nФамилия: {self.surname}" \
               f" \nСредняя оценка за домашние задания: {self.grades}" \
               f" \nКурсы в процессе изучения: {self.courses_in_progress}" \
               f" \nЗавершенные курсы: {self.finished_courses}"


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.teaching_the_course = []
        self.grades = {}
        self.sum_grades = {}

    def __str__(self):
        return f" \nИмя: {self.name}" \
               f" \nФамилия: {self.surname}" \
               f" \nСредняя оценка за лекции: {self.grades}"

    def __eq__(self, other):
        return self.grades == other.grades

    def __lt__(self, other):
        return self.grades < other.grades

    def __gt__(self, other):
        return self.grades > other.grades

    def __le__(self, other):
        return self.grades <= other.grades

    def __ge__(self, other):
        return self.grades >= other.grades

    def average_rating(self, lecturers, course, sum_grades):
        for lecturer in lecturers:
            if isinstance(lecturer, Lecturer) and course in lecturer.grades:
                sum_grades.extend(lecturer.grades[course])
                return


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def __str__(self):
        return f" \nИмя: {self.name}" \
               f" \nФамилия: {self.surname}"

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


some_reviewer = Reviewer('Sam', 'Buddy')
print(some_reviewer)
cool_reviewer = Reviewer('Bob', 'Grovas')
print(cool_reviewer)
some_lecturer = Lecturer('Sam', 'Buddy')
some_lecturer.grades = 9.9
print(some_lecturer)
cool_lecturer = Lecturer('Tomas', 'Redli')
cool_lecturer.grades = 8.5
print(cool_lecturer)
some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.grades = 9.9
some_student.courses_in_progress = 'Python, Git'
some_student.finished_courses = 'Введение в программирование'
print(some_student)
best_student = Student('Mary', 'Yizli', 'your_gender')
best_student.grades = 10
best_student.courses_in_progress = 'Python, Git'
best_student.finished_courses = 'Введение в программирование'
print(best_student)
print(some_lecturer == some_student)
print(some_lecturer < some_student)
print(some_lecturer > some_student)
print(some_lecturer <= some_student)
print(some_lecturer >= some_student)

