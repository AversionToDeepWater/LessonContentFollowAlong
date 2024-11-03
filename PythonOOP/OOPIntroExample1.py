
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade # 0 - 100

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self. name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True #if student added successfully
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)

s1 = Student("Bagel", 20, 90)
s2 = Student("Focaccia", 19, 70)
s3 = Student("Ciabatta", 22, 65)

course = Course("English", 2)

course.add_student(s1)
course.add_student(s2)
print(course.students[1].name)
print(course.add_student(s3)) # won't add another student bc max students is 2
print(course.get_average_grade())