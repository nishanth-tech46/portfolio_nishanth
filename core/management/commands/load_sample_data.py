"""
Django management command to load sample data for the portfolio.
"""
from django.core.management.base import BaseCommand
from core.models import Project, Certification, Skill


class Command(BaseCommand):
    help = 'Load sample data for the portfolio (projects, certifications, skills)'

    def handle(self, *args, **options):
        self.stdout.write('Loading sample data...')

        # Load Skills
        skills_data = [
            # Programming
            {'name': 'Python', 'category': 'programming', 'icon': 'code-2', 'order': 1},
            {'name': 'C', 'category': 'programming', 'icon': 'file-code', 'order': 2},
            {'name': 'C++', 'category': 'programming', 'icon': 'file-code-2', 'order': 3},
            
            # Web
            {'name': 'HTML', 'category': 'web', 'icon': 'layout', 'order': 1},
            {'name': 'CSS', 'category': 'web', 'icon': 'palette', 'order': 2},
            {'name': 'JavaScript', 'category': 'web', 'icon': 'script', 'order': 3},
            
            # Backend
            {'name': 'Django', 'category': 'backend', 'icon': 'server', 'order': 1},
            {'name': 'Flask', 'category': 'backend', 'icon': 'flask-conical', 'order': 2},
            {'name': 'Django REST Framework', 'category': 'backend', 'icon': 'api', 'order': 3},
            {'name': 'JWT', 'category': 'backend', 'icon': 'lock', 'order': 4},
            
            # Database
            {'name': 'MySQL', 'category': 'database', 'icon': 'database', 'order': 1},
            {'name': 'SQLite', 'category': 'database', 'icon': 'database-zap', 'order': 2},
            {'name': 'MySQL Workbench', 'category': 'database', 'icon': 'table', 'order': 3},
            
            # Tools
            {'name': 'Git', 'category': 'tools', 'icon': 'git-branch', 'order': 1},
            {'name': 'GitHub', 'category': 'tools', 'icon': 'github', 'order': 2},
            {'name': 'Netlify', 'category': 'tools', 'icon': 'cloud', 'order': 3},
        ]

        for skill_data in skills_data:
            skill, created = Skill.objects.get_or_create(
                name=skill_data['name'],
                defaults=skill_data
            )
            if created:
                self.stdout.write(f'Created skill: {skill.name}')
            else:
                self.stdout.write(f'Skill already exists: {skill.name}')

        # Load Certifications
        certifications_data = [
            {
                'name': 'Python Full Stack Developer',
                'issuer': 'TechPanda',
                'description': 'Comprehensive full stack development with Python, covering backend development, database integration, and web application deployment.',
            },
            {
                'name': 'Full Stack Python',
                'issuer': 'Skill Intern',
                'description': 'Comprehensive full stack development with Python, covering backend development, database integration, and web application deployment.',
            },
            {
                'name': 'C, C++, Python',
                'issuer': 'Hykin Tech Software Academy',
                'description': 'Programming fundamentals and advanced concepts in C, C++, and Python programming languages.',
            },
            {
                'name': 'Spring Basics',
                'issuer': 'Infosys',
                'description': 'Fundamentals of Spring framework for Java application development.',
            },
            {
                'name': 'Python Problem Solving',
                'issuer': 'L&T',
                'description': 'Advanced problem-solving techniques using Python programming language.',
            },
            {
                'name': 'Basics of Web Development',
                'issuer': 'Infosys',
                'description': 'Fundamental concepts of web development including HTML, CSS, and JavaScript.',
            },
        ]

        for cert_data in certifications_data:
            cert, created = Certification.objects.get_or_create(
                name=cert_data['name'],
                issuer=cert_data['issuer'],
                defaults=cert_data
            )
            if created:
                self.stdout.write(f'Created certification: {cert.name}')
            else:
                self.stdout.write(f'Certification already exists: {cert.name}')

        # Load Projects
        projects_data = [
            {
                'title': 'E-Learning Platform',
                'description': 'A full-stack e-learning platform designed to provide an organized environment for accessing online courses and learning resources.',
                'detailed_description': 'A full-stack e-learning platform for organizing online courses and learning resources.',
                'technologies': 'Python, Django, HTML, CSS, JavaScript',
                'features': 'Django project structure with multiple apps, Course file management, Template-based frontend, SQLite database integration, Static file handling, Media file management for course content',
                'github_repository': 'e_learining_site',
                'github_url': 'https://github.com/nishanth-tech46/e_learining_site',
                'featured': True,
                'order': 1,
            },
            {
                'title': 'Malware Intelligence Using CSV Files',
                'description': 'A Python-based machine-learning project focused on analyzing Android application data using CSV datasets and classification techniques.',
                'detailed_description': 'A Python-based machine-learning project focused on analyzing Android application data from CSV datasets and applying classification techniques to identify potentially malicious applications.',
                'technologies': 'Python, Pandas, NumPy, Scikit-learn, Jupyter Notebook, Random Forest, Support Vector Classifier, CSV',
                'features': 'CSV dataset processing, Data preprocessing, Feature analysis, Machine-learning model training, Classification models, Model evaluation, Prediction workflow',
                'github_repository': 'Malware-intelligence-using-csv-files',
                'featured': False,
                'order': 2,
            },
            {
                'title': 'Library Management System',
                'description': 'A web-based application designed to organize and manage library-related records through a centralized system.',
                'detailed_description': 'A Django-based Library Management System designed to organize library-related operations through a centralized web application. The project uses Django with the library_project app to manage library information. The application includes a books folder for book-related data and uses SQLite for database storage. The system provides a structured interface for working with library records through templates and static files.',
                'technologies': 'Python, Django, HTML, CSS, JavaScript, SQLite',
                'features': 'Django app structure, Book management, Database integration with SQLite, Template-based interface, Static file handling, Library record organization',
                'github_repository': 'Library_management',
                'featured': False,
                'order': 3,
            },
            {
                'title': 'Student Management System',
                'description': 'A web-based application for organizing and managing student records through a structured digital system.',
                'detailed_description': 'A Python-based student grade management system designed to organize and manage student information and grades. The project includes multiple components: grade_system, secondproject, and web-grade-system. The system provides functionality for managing student grades through a Python script (student_grade_management.py) and includes comprehensive project documentation. The application focuses on grade tracking and student record management.',
                'technologies': 'Python',
                'features': 'Student grade management, Grade tracking, Student record organization, Project documentation, Grade system implementation',
                'github_repository': 'student_management',
                'featured': False,
                'order': 4,
            },
            {
                'title': 'Quiz Competition',
                'description': 'An interactive web-based quiz application designed to provide a structured environment for answering questions and participating in quiz activities.',
                'detailed_description': 'A Django-based quiz application providing an interactive environment for creating and taking quizzes. The application features a comprehensive admin panel for quiz and question management, along with a user-facing quiz module. The system includes a dashboard with statistics, quiz management with time limits and passing marks, question management with multiple-choice options, a quiz module with timer and auto-submit, detailed results with scoring and grades, quiz history, and full admin access with search and filters.',
                'technologies': 'Python, Django, SQLite, HTML, CSS, JavaScript',
                'features': 'Dashboard with statistics, Quiz management with time limits, Question management with multiple-choice options, Quiz module with timer countdown, Auto-submit functionality, Detailed results with scoring and grades, Pass/fail status, Answer review, Quiz history, Admin panel with search and filters',
                'github_repository': 'quizzes_compatation',
                'featured': False,
                'order': 5,
            },
        ]

        for project_data in projects_data:
            project, created = Project.objects.get_or_create(
                title=project_data['title'],
                defaults=project_data
            )
            if created:
                self.stdout.write(f'Created project: {project.title}')
            else:
                self.stdout.write(f'Project already exists: {project.title}')

        self.stdout.write(self.style.SUCCESS('Sample data loaded successfully!'))
        self.stdout.write('\nNext steps:')
        self.stdout.write('1. Run: python manage.py createsuperuser')
        self.stdout.write('2. Visit: http://127.0.0.1:8000/admin/')
        self.stdout.write('3. Update project URLs, certification links, and other details in the admin panel')
        self.stdout.write('4. Configure your GitHub and LinkedIn URLs in .env file')
