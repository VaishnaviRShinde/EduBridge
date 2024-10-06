from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Initialize the database and login manager
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)  # Changed _name to _name_
    
    # Configure the app
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  # Change this to your preferred database
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'your_secret_key'  # Set a secret key for session management

    # Initialize extensions with the app
    db.init_app(app)
    login_manager.init_app(app)

    # Define user loader for Flask-Login
    @login_manager.user_loader
    def load_user(user_id):
        from app.models import User  # Import User model here
        return User.query.get(int(user_id))

    # Register Blueprints
    # from app.routes.auth_routes import auth_bp
    from app.routes.teachers_routes import teacher_bp
    from app.routes.student_routes import student_bp
    from app.routes.company_routes import company_bp
    
    # app.register_blueprint(auth_bp)
    app.register_blueprint(teacher_bp, url_prefix='/teacher')
    app.register_blueprint(student_bp, url_prefix='/student')
    app.register_blueprint(company_bp, url_prefix='/company')

    # Import models after initializing the app
    with app.app_context():
        from app import models  # Ensure models are imported here to create tables

    return app