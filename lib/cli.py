import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.helpers import (
    list_teachers, add_teacher, delete_teacher, find_teacher_by_name, view_teacher_students,
    list_students, add_student, delete_student, find_student_by_name, transfer_student, list_students_by_grade,
    show_teacher_workload,
    list_classrooms, add_classroom
)

def welcome():
    print("\n" + "="*60)
    print("  🎓 WELCOME TO THE SCHOOL MANAGEMENT SYSTEM CLI 🎓")
    print("="*60 + "\n")

def main_menu():
    while True:
        print("\nMAIN MENU")
        print("1. Manage Teachers")
        print("2. Manage Students")
        print("3. Manage Classrooms")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            teacher_menu()
        elif choice == '2':
            student_menu()
        elif choice == '3':
            classroom_menu()
        elif choice == '4':
            print("👋 Exiting. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter 1-4.")

def teacher_menu():
    while True:
        print("\nTEACHER MENU")
        print("1. List All Teachers")
        print("2. Add New Teacher")
        print("3. Delete Teacher")
        print("4. Find Teacher by Name")
        print("5. View Teacher's Students")
        print("6. Show Teacher Workload")
        print("7. Back to Main Menu")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            list_teachers()
        elif choice == '2':
            add_teacher()
        elif choice == '3':
            delete_teacher()
        elif choice == '4':
            find_teacher_by_name()
        elif choice == '5':
            view_teacher_students()
        elif choice == '6':
            show_teacher_workload()
        elif choice == '7':
            break
        else:
            print("❌ Invalid choice. Try again.")

def student_menu():
    while True:
        print("\nSTUDENT MENU")
        print("1. List All Students")
        print("2. Add New Student")
        print("3. Delete Student")
        print("4. Find Student by Name")
        print("5. Transfer Student to Another Classroom")
        print("6. List Students by Grade")
        print("7. Back to Main Menu")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            list_students()
        elif choice == '2':
            add_student()
        elif choice == '3':
            delete_student()
        elif choice == '4':
            find_student_by_name()
        elif choice == '5':
            transfer_student()
        elif choice == '6':
            list_students_by_grade()
        elif choice == '7':
            break
        else:
            print("❌ Invalid choice. Try again.")

def classroom_menu():
    while True:
        print("\nCLASSROOM MENU")
        print("1. List All Classrooms")
        print("2. Add New Classroom")
        print("3. Back to Main Menu")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            list_classrooms()
        elif choice == '2':
            add_classroom()
        elif choice == '3':
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    welcome()
    main_menu()
