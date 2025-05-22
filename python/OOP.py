class Student:
    def __init__(self, name, age, subjects):
        self.name = name
        self.age = age
        self.subjects = subjects
        self.average = self.calculate_average()
        self.grade = self.calculate_grade()
    
    def calculate_average(self):
        return sum(self.subjects.values()) / len(self.subjects)
    
    def calculate_grade(self):
        avg = self.average
        if avg >= 90: return "A"
        elif avg >= 80: return "B"
        elif avg >= 70: return "C"
        elif avg >= 60: return "D"
        else: return "F"

class StudentManager:
    def __init__(self):
        self.students = {}
    
    def add_student(self, student_id, student):
        self.students[student_id] = student
    
    def display_all(self):
        for student_id, student in self.students.items():
            print(f"\nID: {student_id}")
            print(f"Name: {student.name}")
            print(f"Age: {student.age}")
            print("Subjects & Marks:")
            for sub, marks in student.subjects.items():
                print(f"  {sub}: {marks}")
            print(f"Average: {student.average:.2f}")
            print(f"Grade: {student.grade}")

# Usage:
manager = StudentManager()
student1 = Student("Alice", 18, {"Math": 95, "Science": 88})
manager.add_student(1, student1)
manager.display_all()