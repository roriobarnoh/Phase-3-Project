from lib.db.models import Base, Teacher, Student, Classroom
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///lib/db/school.db"

def test_db_connection():
    print("Testing database connection...")
    try:
        engine = create_engine(DATABASE_URL)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        print("✅ Database connection successful and tables created (if not exist).")
        session.close()
    except Exception as e:
        print("❌ Database connection failed:", e)

def test_teacher_crud():
    print("\nTesting Teacher CRUD operations...")
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create
    teacher = Teacher(name="Test Teacher", subject="Testing", email="test.teacher@example.com")
    session.add(teacher)
    session.commit()
    print(f"✅ Created Teacher with ID {teacher.id}")

    # Read
    fetched = session.query(Teacher).filter_by(id=teacher.id).first()
    print(f"✅ Fetched Teacher: {fetched.name}, {fetched.subject}, {fetched.email}")

    # Update
    fetched.subject = "Updated Subject"
    session.commit()
    print(f"✅ Updated Teacher subject to: {fetched.subject}")

    # Delete
    session.delete(fetched)
    session.commit()
    print(f"✅ Deleted Teacher with ID {teacher.id}")

    session.close()

def test_student_crud():
    print("\nTesting Student CRUD operations...")
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Need a teacher to assign student to
    teacher = session.query(Teacher).first()
    if not teacher:
        teacher = Teacher(name="Dummy Teacher", subject="Dummy", email="dummy@example.com")
        session.add(teacher)
        session.commit()
        print(f"Created dummy teacher with ID {teacher.id}")

    # Create
    student = Student(name="Test Student", grade="5", teacher_id=teacher.id)
    session.add(student)
    session.commit()
    print(f"✅ Created Student with ID {student.id}")

    # Read
    fetched = session.query(Student).filter_by(id=student.id).first()
    print(f"✅ Fetched Student: {fetched.name}, Grade: {fetched.grade}, Teacher ID: {fetched.teacher_id}")

    # Update
    fetched.grade = "6"
    session.commit()
    print(f"✅ Updated Student grade to: {fetched.grade}")

    # Delete
    session.delete(fetched)
    session.commit()
    print(f"✅ Deleted Student with ID {student.id}")

    session.close()

def test_classroom_crud():
    print("\nTesting Classroom CRUD operations...")
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    teacher = session.query(Teacher).first()
    if not teacher:
        teacher = Teacher(name="Dummy Teacher", subject="Dummy", email="dummy@example.com")
        session.add(teacher)
        session.commit()
        print(f"Created dummy teacher with ID {teacher.id}")

    # Create
    classroom = Classroom(name="Test Classroom", teacher_id=teacher.id)
    session.add(classroom)
    session.commit()
    print(f"✅ Created Classroom with ID {classroom.id}")

    # Read
    fetched = session.query(Classroom).filter_by(id=classroom.id).first()
    print(f"✅ Fetched Classroom: {fetched.name}, Teacher ID: {fetched.teacher_id}")

    # Update
    fetched.name = "Updated Classroom"
    session.commit()
    print(f"✅ Updated Classroom name to: {fetched.name}")

    # Delete
    session.delete(fetched)
    session.commit()
    print(f"✅ Deleted Classroom with ID {classroom.id}")

    session.close()

if __name__ == "__main__":
    test_db_connection()
    test_teacher_crud()
    test_student_crud()
    test_classroom_crud()
    print("\nAll debug tests completed.")

