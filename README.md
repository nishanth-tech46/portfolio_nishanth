# Nishanth K - Python Developer Portfolio

A professional, production-ready portfolio website built with Django, showcasing Python development skills, projects, certifications, and technical expertise.

## Features

- **Responsive Design**: Works seamlessly on mobile, tablet, and desktop devices
- **Dark Theme**: Modern, professional dark developer aesthetic
- **SEO Optimized**: Meta tags, Open Graph metadata, and semantic HTML
- **Contact Form**: AJAX-powered contact form with Django backend validation
- **Admin Panel**: Django admin for managing projects, certifications, skills, and messages
- **Project Showcase**: Dynamic project cards with detailed views
- **Certifications Display**: Professional certification cards
- **Skills Grid**: Organized technology skill categories
- **Smooth Animations**: Subtle, performance-friendly animations
- **Accessibility**: WCAG compliant with keyboard navigation support

## Tech Stack

### Backend
- Python 3.x
- Django 4.2+
- Django REST Framework
- SQLite (development) / MySQL (production-ready)

### Frontend
- HTML5
- CSS3 (Custom CSS with CSS Variables)
- JavaScript (Vanilla ES6+)
- Lucide Icons

### Development Tools
- Git
- Virtual Environment
- Environment Variables (python-dotenv)

## Project Structure

```
newport/
├── manage.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
├── portfolio/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── core/
│   ├── __init__.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── admin.py
│   └── tests.py
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── project_detail.html
│   ├── 404.html
│   └── 500.html
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
└── media/
    └── projects/
```

## Installation

### Prerequisites

- Python 3.8-3.11 (recommended for Django 4.2 compatibility)
- pip (Python package manager)
- Virtual environment (recommended)

**Note**: Python 3.12+ may have test compatibility issues with Django 4.2. The application runs fine, but test suite may require Python 3.8-3.11.

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd newport
```

### Step 2: Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables

Copy the `.env.example` file to `.env` and configure your settings:

```bash
copy .env.example .env
```

Edit `.env` with your configuration:

```env
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1

# Optional: Social Links
GITHUB_URL=https://github.com/yourusername
LINKEDIN_URL=https://linkedin.com/in/yourusername

# Optional: Email Configuration (for contact form)
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

Generate a secret key:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Step 5: Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 6: Create Superuser (Admin)

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

### Step 7: Collect Static Files (Production)

```bash
python manage.py collectstatic
```

### Step 8: Run Development Server

```bash
python manage.py runserver
```

Visit `http://localhost:8000` in your browser.

## Database Models

### Project
- `title`: Project name
- `slug`: URL-friendly identifier (auto-generated)
- `description`: Short project description
- `detailed_description`: Detailed project information
- `technologies`: Comma-separated technology list
- `features`: Comma-separated feature list
- `github_url`: GitHub repository link
- `live_url`: Live demo link
- `image`: Project image
- `featured`: Boolean for featured projects
- `created_at`: Creation timestamp
- `updated_at`: Last update timestamp

### Certification
- `name`: Certification name
- `issuer`: Issuing organization
- `description`: Certification details
- `certificate_url`: Certificate link
- `issued_date`: Issue date

### Skill
- `name`: Skill name
- `category`: Skill category (programming, web, backend, database, tools)
- `icon`: Lucide icon name
- `order`: Display order

### ContactMessage
- `name`: Sender name
- `email`: Sender email
- `subject`: Message subject
- `message`: Message content
- `created_at`: Timestamp
- `status`: Message status (new, read, replied)

## Admin Panel

Access the admin panel at `http://localhost:8000/admin/`

Use the superuser credentials to:
- Manage projects
- Add certifications
- Organize skills
- View contact messages
- Update content

## Running Tests

Run the test suite:

```bash
python manage.py test
```

Run specific test modules:

```bash
python manage.py test core.tests.ProjectModelTest
python manage.py test core.tests.ContactFormTest
```

## Deployment

### Deployment Platforms

This project is ready for deployment on:
- Render
- Railway
- PythonAnywhere
- Heroku (with appropriate configuration)

### Production Configuration

1. Set `DEBUG=False` in `.env`
2. Configure `ALLOWED_HOSTS` with your domain
3. Use a production database (PostgreSQL/MySQL)
4. Configure static file serving
5. Set up email backend for contact form
6. Generate a strong `SECRET_KEY`
7. Configure SSL/HTTPS

### Environment Variables for Production

```env
DEBUG=False
SECRET_KEY=your-production-secret-key
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com

# Database (PostgreSQL example)
DB_NAME=your_database
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your-db-host
DB_PORT=5432

# Email Configuration
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
DEFAULT_FROM_EMAIL=noreply@yourdomain.com
```

### Static Files on Production

For platforms like Render/Railway, static files are handled automatically. For manual deployment:

```bash
python manage.py collectstatic --noinput
```

## Adding Content

### Adding Projects via Admin

1. Go to `/admin/`
2. Navigate to "Projects"
3. Click "Add Project"
4. Fill in:
   - Title
   - Description
   - Detailed description
   - Technologies (comma-separated)
   - Features (comma-separated)
   - GitHub URL (optional)
   - Live URL (optional)
   - Upload image (optional)
   - Mark as featured if desired

### Adding Certifications

1. Go to `/admin/`
2. Navigate to "Certifications"
3. Click "Add Certification"
4. Fill in certification details

### Adding Skills

1. Go to `/admin/`
2. Navigate to "Skills"
3. Click "Add Skill"
4. Fill in skill name, category, icon, and order

## Customization

### Colors

Edit CSS variables in `static/css/style.css`:

```css
:root {
    --bg-primary: #0a0a0f;
    --bg-secondary: #12121a;
    --accent-primary: #3b82f6;
    --accent-secondary: #8b5cf6;
    /* ... */
}
```

### Fonts

Change the font in `templates/base.html`:

```html
<link href="https://fonts.googleapis.com/css2?family=YourFont&display=swap" rel="stylesheet">
```

Update CSS:

```css
:root {
    --font-family: 'YourFont', sans-serif;
}
```

### Content

Update personal information in:
- `templates/home.html` (About section, Education section)
- `templates/base.html` (Footer, Navigation)
- Admin panel (Projects, Certifications, Skills)

## Performance Optimization

- Lazy loading images
- Minimized CSS and JavaScript
- Efficient Django queries
- Static file compression
- Browser caching headers

## Security Features

- CSRF protection
- Secure form handling
- Server-side validation
- Environment variables for secrets
- No hard-coded credentials
- Secure cookie settings (production)
- HSTS configuration (production)

## Accessibility

- Semantic HTML
- Proper heading hierarchy
- ARIA labels
- Keyboard navigation
- Focus states
- Color contrast compliance
- Screen reader friendly
- Reduced motion support

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Future Improvements

- [ ] GitHub API integration for dynamic repository display
- [ ] Blog section
- [ ] Multi-language support
- [ ] Dark/Light theme toggle
- [ ] Project filtering by technology
- [ ] Search functionality
- [ ] Analytics integration
- [ ] PWA support

## Troubleshooting

### Static Files Not Loading

```bash
python manage.py collectstatic
```

Ensure `STATIC_URL` and `STATIC_ROOT` are correctly configured in `settings.py`.

### Database Issues

```bash
python manage.py migrate --run-syncdb
```

Or delete the database and re-run migrations:

```bash
del db.sqlite3
python manage.py migrate
```

### Permission Denied on Linux/macOS

```bash
chmod +x manage.py
```

## License

This project is open source and available for personal and commercial use.

## Contact

For questions or collaboration opportunities, use the contact form on the website or reach out via:
- Email: nishanth@example.com
- GitHub: [Your GitHub Profile]
- LinkedIn: [Your LinkedIn Profile]

---

Built with ❤️ using Django and modern web technologies.
