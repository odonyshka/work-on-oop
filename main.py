class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = []
        self.average_grades = {}

    def rate_lecturer(self, lecturer, course_attached, grade):
        if isinstance(lecturer, Lecturer) and course_attached in lecturer.teaching_the_course and course_attached in lecturer.grade_for_lecturer:
            lecturer.grades[course_attached] += [grade]
        else:
            lecturer.grades[course_attached] = [grade]

    def __str__(self):
        if len(self.grades) > 0:
            avg_grades = sum(self.grades) / len(self.grades)
        else:
            avg_grades = "-"

        in_progress = ""
        for x in self.courses_in_progress:
            in_progress += x + ", "

        finished = ""
        for x in self.finished_courses:
            finished += x + ", "

        some_student = f"Имя: {self.name}, \n"
        some_student += f"Фамилия: {self.surname}, \n"
        some_student += f"Средняя оценка за домашние задания: {avg_grades}, \n"
        some_student += f"Курсы в процессе изучения: {in_progress} \n"
        some_student += f"Завершенные курсы: {finished}"
        return some_student


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.teaching_the_course = []
        self.grades = []
        self.sum_grades = {}

    def __lt__(self, student):
        lecturer = len(self.grades)
        if lecturer == 0:
            return "-"
        else:
            averageLecturer = sum(self.grades) / lecturer

        studentCount = len(student.grades)
        if studentCount == 0:
            return "-"
        else:
            averageStudent = sum(student.grades) / studentCount

        return averageLecturer < averageStudent

    def addGrade(self, grade):
        self.grades.append(grade)

    def __str__(self):
        count = len(self.grades)
        if count == 0:
            average = "-"
        else:
            average = sum(self.grades) / count

        return f"Имя: {self.name} \nФамилия:  {self.surname} \nСредняя оценка за лекции: {average}"


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
best_student = Student('Mary', 'Yizli', 'your_gender')
best_student.grades = 10
best_student.courses_in_progress = 'Python, Git'
best_student.finished_courses = 'Введение в программирование'
print(some_lecturer == some_student)
print(some_lecturer < some_student)
print(some_lecturer > some_student)
print(some_lecturer <= some_student)
print(some_lecturer >= some_student)


