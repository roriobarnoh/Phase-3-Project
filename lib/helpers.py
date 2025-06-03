import re
from tabulate import tabulate
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from lib.db.models import Teacher, Student, Classroom

engine = create_engine("sqlite:///lib/db/school.db")
Session = sessionmaker(bind=engine)
session = Session()

# -----------------------------
# TEACHER FUNCTIONS
# -----------------------------

def list_teachers():
    teachers = session.query(Teacher).all()
    if not teachers:
        print("No teachers found.")
        return

    table = [[t.id, t.name, t.subject, t.email] for t in teachers]
    print("\n👩‍🏫 All Teachers:")
    print(tabulate(table, headers=["ID", "Name", "Subject", "Email"], tablefmt="fancy_grid"))


def add_teacher():
    name = input("Enter teacher's name: ").strip()
    subject = input("Enter subject: ").strip()
    email = input("Enter email: ").strip()
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        print("❌ Invalid email format.")
        return
    new_teacher = Teacher(name=name, subject=subject, email=email)
    session.add(new_teacher)
    session.commit()
    print(f"✅ Teacher '{name}' added successfully.")

def delete_teacher():
    teacher_id = input("Enter teacher ID to delete: ").strip()
    teacher = session.query(Teacher).filter_by(id=teacher_id).first()
    if not teacher:
        print("❌ Teacher not found.")
        return
    confirm = input(f"Are you sure you want to delete {teacher.name}? (y/n): ").lower()
    if confirm == 'y':
        session.delete(teacher)
        session.commit()
        print("✅ Teacher deleted.")
    else:
        print("Cancelled.")

def find_teacher_by_name():
    name = input("Enter teacher name to search: ").strip()
    teachers = session.query(Teacher).filter(Teacher.name.ilike(f"%{name}%")).all()
    if teachers:
        for t in teachers:
            print(f"ID: {t.id}, Name: {t.name}, Subject: {t.subject}, Email: {t.email}")
    else:
        print("❌ No teachers found with that name.")

def view_teacher_students():
    teacher_id = input("Enter teacher ID: ").strip()
    teacher = session.query(Teacher).filter_by(id=teacher_id).first()
    if not teacher:
        print("❌ Teacher not found.")
        return
    if not teacher.students:
        print(f"{teacher.name} has no students.")
        return
    print(f"\nStudents of {teacher.name}:")
    for student in teacher.students:
        print(f"ID: {student.id}, Name: {student.name}, Grade: {student.grade}")

def show_teacher_workload():
    teachers = session.query(Teacher).all()
    for t in teachers:
        count = len(t.students)
        print(f"{t.name} ({t.subject}) has {count} student(s).")

# -----------------------------
# STUDENT FUNCTIONS
# -----------------------------

def list_students():
    students = session.query(Student).all()
    if not students:
        print("No students found.")
        return

    table = []
    for s in students:
        table.append([
            s.id,
            s.name,
            s.grade,
            s.classroom.name if s.classroom else "N/A",
            s.classroom.teacher.name if s.classroom and s.classroom.teacher else "N/A"
        ])

    print("\n👨‍🎓 All Students:")
    print(tabulate(table, headers=["ID", "Name", "Grade", "Classroom", "Teacher"], tablefmt="fancy_grid"))

def add_student():
    name = input("Enter student's name: ").strip()
    grade = input("Enter grade (K-12): ").strip()
    if grade.upper() not in [str(g) for g in range(1, 13)] + ['K']:
        print("❌ Invalid grade. Use K or 1-12.")
        return
    teacher_id = input("Enter teacher ID: ").strip()
    teacher = session.query(Teacher).filter_by(id=teacher_id).first()
    if not teacher:
        print("❌ Teacher not found.")
        return
    new_student = Student(name=name, grade=grade.upper(), teacher_id=teacher.id)
    session.add(new_student)
    session.commit()
    print(f"✅ Student '{name}' added under {teacher.name}.")

def delete_student():
    student_id = input("Enter student ID to delete: ").strip()
    student = session.query(Student).filter_by(id=student_id).first()
    if not student:
        print("❌ Student not found.")
        return
    confirm = input(f"Are you sure you want to delete {student.name}? (y/n): ").lower()
    if confirm == 'y':
        session.delete(student)
        session.commit()
        print("✅ Student deleted.")
    else:
        print("Cancelled.")

def find_student_by_name():
    name = input("Enter student name to search: ").strip()
    students = session.query(Student).filter(Student.name.ilike(f"%{name}%")).all()
    if students:
        for s in students:
            print(f"ID: {s.id}, Name: {s.name}, Grade: {s.grade}, Teacher: {s.teacher.name}")
    else:
        print("❌ No students found with that name.")

def transfer_student():
    student_id = input("Enter student ID to transfer: ").strip()
    student = session.query(Student).filter_by(id=student_id).first()
    if not student:
        print("❌ Student not found.")
        return
    new_teacher_id = input("Enter new teacher ID: ").strip()
    new_teacher = session.query(Teacher).filter_by(id=new_teacher_id).first()
    if not new_teacher:
        print("❌ Teacher not found.")
        return
    student.teacher_id = new_teacher.id
    session.commit()
    print(f"✅ Student '{student.name}' transferred to {new_teacher.name}.")

def list_students_by_grade():
    grade = input("Enter grade to filter by (K-12): ").strip()
    if grade.upper() not in [str(g) for g in range(1, 13)] + ['K']:
        print("❌ Invalid grade.")
        return
    students = session.query(Student).filter_by(grade=grade.upper()).all()
    if students:
        for s in students:
            print(f"ID: {s.id}, Name: {s.name}, Teacher: {s.teacher.name}")
    else:
        print("No students found in this grade.")

# -----------------------------
# CLASSROOM FUNCTIONS
# -----------------------------

def list_classrooms():
    classrooms = session.query(Classroom).all()
    if not classrooms:
        print("No classrooms found.")
        return

    table = []
    for c in classrooms:
        teacher_name = c.teacher.name if c.teacher else "N/A"
        num_students = len(c.students) if hasattr(c, 'students') else "?"
        table.append([c.id, c.name, teacher_name, num_students])

    print("\n🏫 All Classrooms:")
    print(tabulate(table, headers=["ID", "Name", "Teacher", "No. of Students"], tablefmt="fancy_grid"))

def add_classroom():
    name = input("Enter classroom name: ").strip()
    teacher_id = input("Enter teacher ID for this classroom: ").strip()
    teacher = session.query(Teacher).filter_by(id=teacher_id).first()
    if not teacher:
        print("❌ Teacher not found.")
        return
    new_classroom = Classroom(name=name, teacher_id=teacher.id)
    session.add(new_classroom)
    session.commit()
    print(f"✅ Classroom '{name}' added for teacher {teacher.name}.")
