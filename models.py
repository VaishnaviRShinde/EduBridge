from datetime import datetime
from . import db  # Import the db instance from _init_.py

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # student, teacher, company

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    skills_required = db.Column(db.String(120), nullable=False)
    deadline = db.Column(db.DateTime, nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # Companies offering the projects
    teacher_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # Teachers managing projects
    students = db.relationship('User', secondary='student_project')

class Internship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    teacher_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    students = db.relationship('User', secondary='student_internship')

class Certificate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    date_issued = db.Column(db.DateTime, default=datetime.utcnow)

# class Reward(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     student_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     coins = db.Column(db.Integer, nullable=False)

# class Discussion(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
#     student_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     message = db.Column(db.Text, nullable=False)
#     timestamp = db.Column(db.DateTime, default=datetime.utcnow)

# Many-to-Many Relationships
student_project = db.Table('student_project',
    db.Column('student_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('project_id', db.Integer, db.ForeignKey('project.id'))
)

student_internship = db.Table('student_internship',
    db.Column('student_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('internship_id', db.Integer, db.ForeignKey('internship.id'))
)