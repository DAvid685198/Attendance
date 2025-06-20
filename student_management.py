
def add_student_record():
    roll_no = input("Enter Your Roll No")
    name = input("Enter Your Name")
    contact_no = input("Enter Your Contact No")

    with open("student.txt", "r") as student_record:
        students = student_record.readlines()
        for student in students:
            student =  student.strip()
            if student.startswith(f"{roll_no}"+","):
                print("student with this roll no already exist")
                return
    
    with open("student.txt", "a") as file:
        file.write(f"{roll_no},{name},{contact_no}\n")
    print("Student Record Added Successfully")
    
def view_student_record():
    with open("student.txt", "r") as student_data:
        students = student_data.readlines()
        for student in students:
            print(student.strip())

def update_student_record():
    roll_no = input("Enter Student Roll No: ")

    is_update = False
    update_record = []
    #step 1 read student record
    with open ("student.txt", "r") as file:
        students = file.readlines()
        for student in students:
            student_record = student.strip().split(",")

            student_roll = student_record[0]

            if student_roll == roll_no:
                print(f"student Record: {student_record}")
                name = input("Enter Your Name: ")
                contact_no = input("Enter Your Contact No: ")
                update_record.append(f"{roll_no}, {name}, {contact_no}")
                is_update = True
            else:
                update_record.append(student)
        if is_update:
            with open("student.txt", "w") as file:
                file.writelines(update_record)
            print("student record updated sucessfully.")
        else:
            print("student record not found.")


def delete_student():
     roll_no = input("Enter Student Roll No to Delete: ")
     is_deleted = False
     updated_records = []

    # Step 1: Read student records
     with open("student.txt", "r") as file:
        students = file.readlines()
        for student in students:
            student_record = student.strip().split(",")
            student_roll = student_record[0]

            # Check if the roll number matches
            if student_roll == roll_no:
                print(f"student records: {student_record}")
                is_deleted = True
                # Skip adding this record to updated_records to delete it
            else:
                updated_records.append(student)

    # Step 2: Write updated records back to the file
     if is_deleted:
        with open("student.txt", "w") as file:
            file.writelines(updated_records)
        print("Student record deleted successfully.")
     else:
        print("Student record not found.")

   
   
   
   
   
   # print("You are on Delete Student")