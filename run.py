from flask import Flask
from flask_login import LoginManager
from app.models import User  # Import your User model
from app.routes.student_routes import student_bp as student   # Adjust the import path if needed
from app.routes.teachers_routes import teacher_bp as teacher  # Adjust the import path if needed
from app.routes.company_routes import company_bp as company   # Adjust the import path if needed

# Initialize the Flask application
app = Flask(__name__)  # Corrected _name to _name_

# Configure your app (add your configurations here)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with your secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Replace with your database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

# Define how to load the user (customize this according to your User model)
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Register Blueprints
app.register_blueprint(student, url_prefix='/student')
app.register_blueprint(teacher, url_prefix='/teacher')
app.register_blueprint(company, url_prefix='/company')

# Run the application
if __name__ == '_main':  # Corrected _name to _name_
    app.run(debug=True)  # Set debug=False in production