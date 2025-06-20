from student_management import (
    add_student_record, update_student_record,
    view_student_record, delete_student
)
from attendance_management import (
    take_attendance,
    view_attendance,
)

def menu():
    run = True
    while run:
        print("Enter 1 to add student")
        print("Enter 2 to view student details")
        print("Enter 3 to update student")
        print("enter 4 to Delete student")
        print("Enter 5 to take Attendance")
        print("Enter 6 to view Attendance")
        print("Enter 7 to end")
        option = input("enter menu no: ")
        if option == "1":
            add_student_record()
        elif option == "2":
            view_student_record()
        elif option == "3":
            update_student_record()
        elif option == "4":
            delete_student()
        elif option == "5":
            take_attendance()
        elif option == "6":
            view_attendance()
        elif option == "7":
            run = False
        else:
            print("invalid choices")
menu()

