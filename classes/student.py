from classes.person import Person
import csv

class Student(Person):
    def __init__(self, name, age, role, password, school_id) -> None:
        super().__init__(name, age, role, password)
        self.school_id = school_id

    def __str__(self) -> str:
        return f"\n{self.name.capitalize()}\n---------------\nAge: {self.age}\nID: {self.school_id}"
    
    # def to_string(self) -> str:
    #     student_dict = {'name': self.name}

    @staticmethod
    def all_students():
        # return contents of student.csv
        with open('data/students.csv', newline='') as file:
            csv_reader = csv.DictReader(file, skipinitialspace=True)
            students = [row for row in csv_reader]
            file.close()
        
        return students