import uuid
import sys
#TODO 1
print("Name : Ruba Naim")
print("Delivery Date :3/7/2023\n")

#TODO 2
class Course:
    def __init__(self, course_name, course_mark):
        self.course_id = uuid.uuid4()
        self.course_name = course_name
        self.course_mark = course_mark


class Student:
# TODO 3
    total_students = 0

# TODO 4
    def __init__(self, student_name, student_age, student_number):
        self.student_id = uuid.uuid4()
        self.student_name = student_name
        self.student_age = student_age
        self.student_number = student_number
        self.courses_list = []
        Student.total_students+=1

# TODO 5
    def enroll_course(self, course_name, course_mark):
        course = Course(course_name, course_mark)
        self.courses_list.append(course)

# TODO 6
    def get_student_details(self):
        return self.__dict__

    def get_student_courses(self):
        for course in self.courses_list:
            print(f"Course Name: {course.course_name}, Course Mark: {course.course_mark}")
 # TODO 7
    def get_student_average(self):
        total_marks = 0
        for course in self.courses_list:
            total_marks += course.course_mark
        if len(self.courses_list) > 0:
            return total_marks / len(self.courses_list)
        else:
            return 0

 # TODO 8
students = []
# TODO 9
while True:
    # TODO 10
    try:
        selection = int(input("\n1.Add New Student\n"
                              "2.Delete Student\n"
                              "3.Display Student\n"
                              "4.Get Student Average\n"
                              "5.Add Course to Student with Mark\n"
                              "6.Exit\n\n"))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if selection == 1:
        student_number = input("Enter Student Number: ")
        if any(student.student_number == student_number for student in students):
            print("Student Number already exists.")
            continue

        student_name = input("Enter Student Name: ")
        while True:
            try:
                student_age = int(input("Enter Student Age: "))
                break
            except ValueError:
                print("Invalid Age. Please enter a valid number.")
 # TODO 11
        student = Student(student_name, student_age, student_number)
        students.append(student)
        print("Student Added Successfully")
 # TODO 12
    elif selection == 2:
        student_number = input("Enter Student Number: ")
        for student in students:
            if student.student_number == student_number:
                students.remove(student)
                print("Student Deleted Successfully")
                break
        else:
            print("Student Not Exist")
 # TODO 13
    elif selection == 3:
        student_number = input("Enter Student Number: ")
        for student in students:
            if student.student_number == student_number:
                print("Student Details:")
                print(f"Student ID: {student.student_id}")
                print(f"Student Name: {student.student_name}")
                print(f"Student Age: {student.student_age}")
                print(f"Student Number: {student.student_number}")
                print("Courses:")
                student.get_student_courses()
                break
        else:
            print("Student Not Exist")

 # TODO 14
    elif selection == 4:
        student_number = input("Enter Student Number: ")
        for student in students:
            if student.student_number == student_number:
                average = student.get_student_average()
                print(f"Student Average: {average}")
                break
        else:
            print("Student Not Exist")

 # TODO 15
    elif selection == 5:
        student_number = input("Enter Student Number: ")
        for student in students:
            if student.student_number == student_number:
                course_name = input("Enter Course Name: ")
                while True:
                    try:
                        course_mark = float(input("Enter Course Mark: "))
                        break
                    except ValueError:
                        print("Invalid input.")
                course=Course(course_name, course_mark)
                student.courses_list.append(course)

    # TODO 16
    elif selection==6:
        print("Existing the program..")
        sys.exit(0)