class Person:
    def __init__(self, full_name, age, is_married='No'):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f'Full name: {self.full_name}. Age: {self.age}. Married: {self.is_married}.')

print("Класс Person")
person1 = Person("Elmira", 17)
person1.introduce_myself()

class Student(Person):
    def __init__(self, full_name, age, is_married, marks):
        super().__init__(full_name, age, is_married)
        self.marks = marks

    def average_marks(self):
        return sum(self.marks.values()) / len(self.marks)

    def introduce_myself(self):
        super().introduce_myself()
        print(f'Marks: {self.marks}')
        for subject, mark in self.marks.items():
            print(f'{subject}: {mark}')
        print(f'Average marks: {self.average_marks():.2f}\n')

print("\nКласс Student наслед. Person")
student1 = Student('Ariana', 18, 'No', {'math': 5, 'english': 5, 'physics': 4, 'chemistry': 3, 'biology': 3, 'literature': 5})
student1.introduce_myself()

class Teacher(Person):
    base_salary = 30000

    def __init__(self, full_name, age, is_married, experience):
        super().__init__(full_name, age, is_married)
        self.experience = experience

    def salary(self):
        bonus_years = max(0, self.experience - 3)
        bonus = self.base_salary * 0.05 * bonus_years
        return self.base_salary + bonus

    def introduce_myself(self):
        super().introduce_myself()
        print(f'Experience: {self.experience} years.')
        print(f'Salary: ${self.salary():.2f}\n')

print("\nКласс Teacher наслед. Person")
teacher1 = Teacher('Koralina', 30, 'Yes', 5)
teacher1.introduce_myself()

def create_students():
    return [
        Student('Alihan', 19, 'No', {'math': 4, 'english': 5, 'physics': 3}),
        Student('Maria', 18, 'No', {'math': 5, 'english': 4, 'physics': 5}),
        Student('Nura', 20, 'No', {'math': 3, 'english': 4, 'physics': 4})
    ]

print("Функция create_students")
students = create_students()
for student in students:
    student.introduce_myself()
