# app/routes/teacher_routes.py

from flask import Blueprint, request, jsonify, render_template
from flask_login import login_required, current_user
from app.models import Project, db  # Import Project and db from models
from app.models import User, Internship  # Import User and Internship if needed

# Initialize the Blueprint
teacher_bp = Blueprint('teacher', __name__)

@teacher_bp.route('/teacher')
@login_required
def teacher():
    return render_template('teacher.html')

@teacher_bp.route('/teacher/dashboard')
@login_required
def teacher_dashboard():
    # Fetch teacher-specific classes or projects from the database
    projects = Project.query.filter_by(teacher_id=current_user.id).all()
    return render_template('teacher.html', projects=[p.serialize() for p in projects])

@teacher_bp.route('/upload_project', methods=['POST'])
@login_required
def upload_project():
    data = request.get_json()
    
    new_project = Project(
        title=data['title'], 
        description=data['description'], 
        skills_required=data['skills_required'],
        deadline=data['deadline'],
        company_id=data['company_id'],
        teacher_id=current_user.id
    )
    
    db.session.add(new_project)
    db.session.commit()
    
    return jsonify({'message': 'Project uploaded successfully'})

@teacher_bp.route('/students_status', methods=['GET'])
@login_required
def student_status():
    projects = Project.query.filter_by(teacher_id=current_user.id).all()
    
    return jsonify({'projects': [p.serialize() for p in projects]})