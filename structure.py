class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def display_details(self):
        print("\n--- Student Details ---")
        print(f"Roll Number: {self.roll_no}")
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks:.2f}")

# Get student input
try:
    roll_no_str = input("Enter student roll number: ")
    roll_no = int(roll_no_str)

    name = input("Enter student name: ")

    marks_str = input("Enter student marks: ")
    marks = float(marks_str)

    # Create a Student object
    student = Student(roll_no, name, marks)

    # Display student details
    student.display_details()

except ValueError:
    print("Invalid input. Please ensure roll number is an integer and marks are a number.")