# app/routes/student_routes.py

from flask import Blueprint, request, jsonify, render_template
from flask_login import login_required, current_user
from app.models import Project, Internship,  db

student_bp = Blueprint('student', __name__)

@student_bp.route('/student')
@login_required
def student():
    return render_template('student.html')

@student_bp.route('/student/dashboard')
@login_required
def student_dashboard():
    # Fetch projects and internships from the database
    projects = Project.query.all()
    internships = Internship.query.all()
    
    # Render the dashboard template with the fetched data
    return render_template('student_dashboard.html', 
                           projects=[p.serialize() for p in projects],
                           internships=[i.serialize() for i in internships])



@student_bp.route('/apply', methods=['POST'])
@login_required
def apply():
    data = request.get_json()
    project_id = data.get('project_id')
    internship_id = data.get('internship_id')

    if project_id:
        project = Project.query.get(project_id)
        project.students.append(current_user)
        db.session.commit()
        return jsonify({'message': 'Applied to project successfully'})
    
    if internship_id:
        internship = Internship.query.get(internship_id)
        internship.students.append(current_user)
        db.session.commit()
        return jsonify({'message': 'Applied to internship successfully'})

@student_bp.route('/progress', methods=['GET'])
@login_required
def view_progress():
    # View all the applied projects and progress
    student_projects = current_user.projects
    student_internships = current_user.internships
    return jsonify({'projects': [p.serialize() for p in student_projects], 
                    'internships': [i.serialize() for i in student_internships]})

# @student_bp.route('/discuss/<int:project_id>', methods=['POST'])
# @login_required
# def post_discussion(project_id):
#     data = request.get_json()
#     message = data.get('message')
#     new_discussion = Discussion(project_id=project_id, student_id=current_user.id, message=message)
#     db.session.add(new_discussion)
#     db.session.commit()
#     return jsonify({'message': 'Message posted successfully!'})