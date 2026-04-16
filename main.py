import random

students = []

def add_student():
    name = input("Enter student name: ")
    
    try:
        fee = float(input("Enter monthly fee: "))
    except:
        print("Invalid fee. Try again.\n")
        return

    student = {
        "id": random.randint(1000, 9999),
        "name": name,
        "fee": fee,
        "paid": 0
    }

    students.append(student)
    print("Student added successfully!\n")


def view_students():
    if not students:
        print("No students found.\n")
        return

    print("\n--- Students List ---")
    for s in students:
        balance = s["fee"] - s["paid"]
        print(f"ID: {s['id']} | Name: {s['name']} | Fee: {s['fee']} | Paid: {s['paid']} | Balance: {balance}")
    print()


def record_payment():
    if not students:
        print("No students available.\n")
        return

    view_students()

    try:
        student_id = int(input("Enter student ID: "))
        amount = float(input("Enter payment amount: "))
    except:
        print("Invalid input.\n")
        return

    for s in students:
        if s["id"] == student_id:
            s["paid"] += amount
            print("Payment recorded successfully!\n")
            return

    print("Student not found.\n")


def main_menu():
    while True:
        print("=== Student Management System ===")
        print("1. Add Student")
        print("2. View Students")
        print("3. Record Payment")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            record_payment()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.\n")


def main():
    main_menu()


if __name__ == "__main__":
    main()