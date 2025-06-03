from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.db.models import Base, Teacher, Student, Classroom
from tabulate import tabulate

# Initialize DB
engine = create_engine("sqlite:///lib/db/school.db")
Session = sessionmaker(bind=engine)
session = Session()

# Clear existing data
session.query(Student).delete()
session.query(Classroom).delete()
session.query(Teacher).delete()
session.commit()

# Seed Teachers
teachers = [
    Teacher(name="Alice Johnson", subject="Math", email="alice.johnson@example.com"),
    Teacher(name="Brian Smith", subject="English", email="brian.smith@example.com"),
    Teacher(name="Carol Martinez", subject="Science", email="carol.martinez@example.com"),
    Teacher(name="David Lee", subject="History", email="david.lee@example.com"),
    Teacher(name="Eva Chen", subject="Art", email="eva.chen@example.com"),
]
session.add_all(teachers)
session.commit()

# Seed Classrooms
classrooms = [
    Classroom(name="Room A", teacher=teachers[0]),
    Classroom(name="Room B", teacher=teachers[1]),
    Classroom(name="Room C", teacher=teachers[2]),
]
session.add_all(classrooms)
session.commit()

# Seed Students
students = [
    Student(name="Liam Parker", grade="3", classroom=classrooms[0]),
    Student(name="Sophia Kim", grade="4", classroom=classrooms[0]),
    Student(name="Noah Wright", grade="5", classroom=classrooms[1]),
    Student(name="Olivia Green", grade="2", classroom=classrooms[1]),
    Student(name="Mason Hall", grade="K", classroom=classrooms[2]),
    Student(name="Emma Lewis", grade="1", classroom=classrooms[2]),
    Student(name="James Scott", grade="6", classroom=classrooms[0]),
    Student(name="Ava Young", grade="7", classroom=classrooms[1]),
    Student(name="Lucas Rivera", grade="8", classroom=classrooms[2]),
    Student(name="Mia Perez", grade="9", classroom=classrooms[0]),
]
session.add_all(students)
session.commit()

print("✅ Seed data inserted successfully.\n")

# Tabular summary
def print_summary():
    print("👩‍🏫 Teachers:")
    teacher_data = [[t.id, t.name, t.subject, t.email] for t in session.query(Teacher).all()]
    print(tabulate(teacher_data, headers=["ID", "Name", "Subject", "Email"], tablefmt="fancy_grid"))

    print("\n🏫 Classrooms:")
    classroom_data = [[c.id, c.name, c.teacher.name if c.teacher else "N/A"] for c in session.query(Classroom).all()]
    print(tabulate(classroom_data, headers=["ID", "Name", "Teacher"], tablefmt="fancy_grid"))

    print("\n👨‍🎓 Students:")
    student_data = [
        [s.id, s.name, s.grade, s.classroom.name if s.classroom else "N/A"]
        for s in session.query(Student).all()
    ]
    print(tabulate(student_data, headers=["ID", "Name", "Grade", "Classroom"], tablefmt="fancy_grid"))

print_summary()

