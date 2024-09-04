class Person:

    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_yourself(self):
        print(f'Fullname: {self.fullname},\nAge: {self.age},\nIs married: {self.is_married}')


class Student(Person):

    def __init__(self, fullname, age, is_married, marks: dict):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def average_note(self):
        the_average_note = round(sum(self.marks.values()) / len(self.marks.values()), 2)
        print(f'The average note of {self.fullname}: {the_average_note}')


class Teacher(Person):

    base_salary = 30000

    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.experience = experience

    def individual_salary(self):
        if self.experience > 3:
            salary = Teacher.base_salary
            for i in range(self.experience - 3):
                salary += salary / 100 * 5
            print(f"The salary of {self.fullname}: {salary}")
        else:
            print(f"The salary of {self.fullname}: {Teacher.base_salary}")


Natalya_teacher = Teacher("Shishkina Natalya Dmitrievna", 35, "yes", 5)
Natalya_teacher.introduce_yourself()
Natalya_teacher.individual_salary()


def create_students():
    Dima_student = Student("Sharashkin Dmitriy Vladimirovich", 18, "no", {"Mathematics": 4, "History": 5, "English": 4})
    Sanya_student = Student("Galkin Alexandre Antonovich", 19, "no", {"Mathematics": 5, "History": 3, "English": 4, "Geometry": 5})
    Andryuha_student = Student("Voronov Andrey Vsevolodovich", 19, "no", {"Mathematics": 3, "History": 5, "Russian": 4, "Geometry": 3})
    students = [Dima_student, Sanya_student, Andryuha_student]
    return students


for student in create_students():
    student.introduce_yourself()
    for subject, note in student.marks.items():
        print(f'Subject: {subject}, note: {note}')
    student.average_note()
