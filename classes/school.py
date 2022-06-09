from classes.student import Student
from classes.staff import Staff

class School:
    def __init__(self, name) -> None:
        self.name = name
        self.students = Student.all_students()
        self.staff = Staff.all_staff()

    def __str__(self) -> str:
        print(f"{self.name.upper()}")

    def list_students(self) -> str:
        print("\nAll students:\n---------------")
        for i, student in enumerate(self.students):
            print(f"{i+1}. {student['name'].capitalize()} {student['school_id']}")

    def find_student_by_id(self, student_id) -> str:
        for student in self.students:
            if(student['school_id'] == student_id):
                return student

    def add_student(self, student_data):
        new_student = Student(student_data['name'], student_data['age'], student_data['role'], student_data['password'], student_data['school_id'])
        self.students.append(new_student)
        return self.list_students()


    def remove_student(self, student_id):
        pass