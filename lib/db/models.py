from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, validates
from sqlalchemy.ext.declarative import declarative_base
import re

Base = declarative_base()

class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    subject = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    students = relationship('Student', back_populates='teacher')

    classrooms = relationship("Classroom", back_populates="teacher", cascade="all, delete")

    def __repr__(self):
        return f"<Teacher(id={self.id}, name='{self.name}', subject='{self.subject}', email='{self.email}')>"

    @validates('email')
    def validate_email(self, key, address):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", address):
            raise ValueError("Invalid email format")
        return address


class Classroom(Base):
    __tablename__ = 'classrooms'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))

    teacher = relationship("Teacher", back_populates="classrooms")
    students = relationship("Student", back_populates="classroom", cascade="all, delete")

    def __repr__(self):
        return f"<Classroom(id={self.id}, name='{self.name}', teacher_id={self.teacher_id})>"


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    grade = Column(String, nullable=False)
    classroom_id = Column(Integer, ForeignKey('classrooms.id'))
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True) 

    teacher = relationship('Teacher', back_populates='students')
    classroom = relationship("Classroom", back_populates="students")

    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}', grade='{self.grade}', classroom_id={self.classroom_id})>"

    @validates('grade')
    def validate_grade(self, key, grade):
        valid_grades = [str(g) for g in range(1, 13)] + ['K']
        if grade not in valid_grades:
            raise ValueError("Grade must be one of: K, 1–12")
        return grade
