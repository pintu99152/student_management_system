from classroom import ClassRoom


class StudentManager(ClassRoom):

    def __init__(self):
        self.students = []

    def add_student(self, roll, name, marks):
        abc = ClassRoom(roll, name, marks)
        self.students.append(abc)
        print("\nStudent Added Successfully.")

    def display_student(self):
        if len(self.students) == 0:
            print("No Student Added")
        else:
            count = 1
            for s in self.students:
                print(f"\nStudent {count}")
                print(f"Roll No. : {s.roll}, Name : {s.name}, Marks : {s.marks}")
                count += 1

    def search_student(self, roll):
        for s in self.students:
            if s.roll == roll:
                print(
                    f"\nStudent Found --> Roll No. : {s.roll}, "
                    f"Name : {s.name}, Marks : {s.marks}"
                )
                return

        print("\nStudent Not Found.")

    def update_student(self, roll):
        for s in self.students:
            if s.roll == roll:
                print("\nStudent Found!")

                s.name = input("Enter new name: ")
                s.marks = float(input("Enter new marks: "))

                print("\nStudent Updated Successfully.")
                return

        print("\nStudent Not Found.")

    def delete_student(self, roll):
        for s in self.students:
            if s.roll == roll:
                self.students.remove(s)
                print("\nStudent Deleted Successfully.")
                return

        print("\nStudent Not Found.")