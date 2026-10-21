# Dictionary used to store student names and their scores
students = {
    "Alice": 80,
    "Bob": 65
}

import json


def add_student():
    """Add a new student and their score to the dictionary."""
    name = input("\nEnter name: ")

    # Keep asking until a valid integer score is entered
    while True:
        try:
            score = int(input("Enter score: "))
            break
        except ValueError:
            print("Int required")

    students[name] = score


def view_students():
    """Display all students and their scores."""
    print()

    if len(students) == 0:
        print("There are no students")

    # Loop through every student in the dictionary
    for name, score in students.items():
        print(f"{name}: {score}")


def highest_score():
    """Find and return the highest score and the student's name."""
    high_score = None
    high_student = None

    # Compare every score to find the highest
    for name, score in students.items():
        if high_score is None or score > high_score:
            high_score = score
            high_student = name

    return high_score, high_student


def average_score():
    """Calculate and return the average student score."""
    total = 0
    count = 0

    # Add all scores together and count students
    for score in students.values():
        total += score
        count += 1

    try:
        average = total / count
        return average
    except ZeroDivisionError:
        print("No students")


def remove_student():
    """Remove a student from the dictionary."""
    student = input("\nWho would you like to remove: ")

    try:
        students.pop(student)
        print("Student removed")
    except KeyError:
        print("Student not found in dictionary")


def save_students():
    """Save all student data to a JSON file."""
    file = open("students3.json", "w")
    json.dump(students, file)
    file.close()

    print("\nStudents saved")


def load_students():
    """Load student data from a JSON file."""
    global students

    try:
        file = open("students3.json", "r")
        students = json.load(file)
        file.close()

        print("\nStudents loaded")
    except FileNotFoundError:
        print("\nNo save file found")


def lowest_score():
    """Find and return the lowest score and the student's name."""
    low_mark = None
    low_student = None

    # Compare every score to find the lowest
    for name, score in students.items():
        if low_mark is None or low_mark > score:
            low_mark = score
            low_student = name

    return low_mark, low_student


def search_student():
    """Search for a student by name."""
    student = input("\nWho are you searching for: ")

    # Check each student name until a match is found
    for name, score in students.items():
        if student == name:
            print(f"\n{student} has a score of {score}")
            return

    print("\nStudent not found")


def update_score():
    """Update the score of an existing student."""
    student = input("\nWho's score would you like to update: ")

    for name, score in students.items():
        if student == name:
            try:
                new_score = int(input("Updated score: "))
                students[name] = new_score
                return
            except ValueError:
                print("Invalid input try again later")
                return

    print("Student not found")


def class_statistics():
    """Return a summary of class statistics."""
    if len(students) == 0:
        return

    count = len(students)
    average = average_score()
    high_score, high_student = highest_score()
    low_score, low_student = lowest_score()

    return count, average, high_score, high_student, low_score, low_student


def main():
    """Main menu loop for the student management system."""
    while True:
        # Display menu options
        print("\n1. Add student")
        print("2. View students")
        print("3. Find highest score")
        print("4. Exit")
        print("5. Average score")
        print("6. Remove student")
        print("7. Save students")
        print("8. Load students")
        print("9. Find lowest score")
        print("10. Search for a student")
        print("11. Update a score")
        print("12. Class statistics")

        option = input(":")

        match option:
            case "1":
                add_student()

            case "2":
                view_students()

            case "3":
                high_score, high_student = highest_score()
                print(f"\nHighest scorer: {high_student}")
                print(f"Score: {high_score}")

            case "4":
                print("\nGoodbye")
                exit()

            case "5":
                average = average_score()
                print(f"\nAverage score: {average:.2f}")

            case "6":
                remove_student()

            case "7":
                save_students()

            case "8":
                load_students()

            case "9":
                low_mark, low_student = lowest_score()
                print(f"Lowest student: {low_student}")
                print(f"Score: {low_mark}")

            case "10":
                search_student()

            case "11":
                update_score()

            case "12":
                try:
                    count, average, high_score, high_student, low_score, low_student = class_statistics()

                    print(f"\nStudents: {count}")
                    print(f"Average: {average:.2f}")
                    print(f"Highest: {high_student} ({high_score})")
                    print(f"Lowest: {low_student} ({low_score})")

                except TypeError:
                    print("\nThere are no students")

            case _:
                print("\nInvalid input")


if __name__ == "__main__":
    main()