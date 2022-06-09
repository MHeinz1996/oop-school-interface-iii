from gettext import find
from classes.school import School
from classes.student import Student

school = School('Ridgemont High')

mode = None
while(mode != '5'):
    mode = input("\nWhat would you like to do?\nOptions:\n1. List All Students\n2. View Individual Student <student_id>\n3. Add a Student\n4. Remove a Student <student_id>\n5. Quit\n> ")

    if mode == '1':
        school.list_students()
    elif mode == '2':
        student_id = input('Enter student id:\n> ')
        find_student = school.find_student_by_id(student_id)
        student = Student(find_student['name'], find_student['age'], find_student['role'], find_student['password'], find_student['school_id']) # Was having trouble passing a dictionary as a class arg
        print(student)
    else:
        pass