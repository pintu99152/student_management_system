from student_manager import StudentManager

manager = StudentManager()

while True:
    print("\n------------------------------------------------------------------")
    print("------------------- STUDENT MANAGEMENT SYSTEM -------------------")
    print("------------------------------------------------------------------")

    print("\n1. Add Student")
    print("2. Display Student")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit\n")

    choice = input("Enter your Choice: ")

    if choice == "1":
        roll = int(input("Enter your roll number: "))
        name = input("Enter your name: ")
        marks = float(input("Enter your marks: "))
        manager.add_student(roll, name, marks)

    elif choice == "2":
        manager.display_student()

    elif choice == "3":
        roll = int(input("Enter your roll number: "))
        manager.search_student(roll)

    elif choice == "4":
        roll = int(input("Enter your roll number: "))
        manager.update_student(roll)

    elif choice == "5":
        roll = int(input("Enter your roll number: "))
        manager.delete_student(roll)

    elif choice == "6":
        print("\nDhanyavaad!")
        break

    else:
        print("\nPlease enter a valid number.")