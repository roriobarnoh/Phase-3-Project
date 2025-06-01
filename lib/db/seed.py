from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.db.models import Base, Teacher, Student, Classroom

# Initialize DB
engine = create_engine("sqlite:///lib/db/school.db")
Session = sessionmaker(bind=engine)
session = Session()

# Clear existing data (optional for reseeding)
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

# Seed Classrooms (1 classroom per teacher, total 3 classrooms only for now)
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

print("✅ Seed data inserted successfully.")
