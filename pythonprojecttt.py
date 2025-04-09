def add_student():
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    course = input("Enter student course: ")

    student = {
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    print(f"Student {name} added successfully!\n")


def view_students():
    if not students:
        print("No students found.\n")
        return

    print("Student List:")
    for i, student in enumerate(students, start=1):
        print(f"{i}. Name: {student['name']}, Age: {student['age']}, Course: {student['course']}")
    print()


def search_student():
    name = input("Enter student name to search: ")
    found = False

    for student in students:
        if student["name"].lower() == name.lower():
            print(f"Student Found: Name: {student['name']}, Age: {student['age']}, Course: {student['course']}\n")
            found = True
            break

    if not found:
        print("Student not found.\n")


def update_student():
    name = input("Enter student name to update: ")
    for student in students:
        if student["name"].lower() == name.lower():
            student["age"] = input("Enter new age: ")
            student["course"] = input("Enter new course: ")
            print(f"Student {name} updated successfully!\n")
            return

    print("Student not found.\n")


def delete_student():
    name = input("Enter student name to delete: ")
    for student in students:
        if student["name"].lower() == name.lower():
            students.remove(student)
            print(f"Student {name} deleted successfully!\n")
            return

    print("Student not found.\n")


import json


def save_data():
    with open("students.json", "w") as file:
        json.dump(students, file)
    print("Data saved successfully!\n")


def load_data():
    global students
    try:
        with open("students.json", "r") as file:
            students = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        students = []  # If file doesn't exist, initialize as empty list


def main():
    load_data()  # Load data when the program starts

    while True:
        print("Student Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Save Data")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            save_data()
        elif choice == "7":
            print("Exiting... Goodbye!")
            save_data()
            break
        else:
            print("Invalid choice! Please try again.\n")


if __name__ == "__main__":
 main()