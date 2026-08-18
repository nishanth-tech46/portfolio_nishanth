"""
Views for the portfolio.
"""
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST
from .models import Project, Certification, Skill
from .forms import ContactForm


def home(request):
    """Home page view."""
    featured_projects = Project.objects.filter(featured=True)[:5]
    all_projects = Project.objects.all()[:5]
    certifications = Certification.objects.all()
    skills = Skill.objects.all()
    
    context = {
        'featured_projects': featured_projects,
        'all_projects': all_projects,
        'certifications': certifications,
        'skills': skills,
        'github_url': getattr(settings, 'GITHUB_URL', ''),
        'github_username': getattr(settings, 'GITHUB_USERNAME', ''),
        'linkedin_url': getattr(settings, 'LINKEDIN_URL', ''),
        'contact_email': getattr(settings, 'CONTACT_EMAIL', ''),
    }
    return render(request, 'home.html', context)


def project_detail(request, slug):
    """Project detail view."""
    project = get_object_or_404(Project, slug=slug)
    
    # Construct GitHub URL if repository is set but URL is not
    if project.github_repository and not project.github_url:
        github_username = getattr(settings, 'GITHUB_USERNAME', '')
        if github_username:
            project.github_url = f'https://github.com/{github_username}/{project.github_repository}'
    
    context = {
        'project': project,
        'github_url': getattr(settings, 'GITHUB_URL', ''),
        'github_username': getattr(settings, 'GITHUB_USERNAME', ''),
        'linkedin_url': getattr(settings, 'LINKEDIN_URL', ''),
        'contact_email': getattr(settings, 'CONTACT_EMAIL', ''),
    }
    return render(request, 'project_detail.html', context)


@csrf_protect
@require_POST
def contact_submit(request):
    """Handle contact form submission via AJAX."""
    form = ContactForm(request.POST)
    
    if form.is_valid():
        contact_message = form.save()
        
        # Send email notification
        try:
            receiver_email = getattr(settings, 'CONTACT_RECEIVER_EMAIL', settings.DEFAULT_FROM_EMAIL)
            send_mail(
                f'Portfolio Contact: {contact_message.subject}',
                f'Name: {contact_message.name}\n'
                f'Email: {contact_message.email}\n'
                f'Subject: {contact_message.subject}\n\n'
                f'Message:\n{contact_message.message}',
                settings.DEFAULT_FROM_EMAIL,
                [receiver_email],
                fail_silently=False,
            )
        except Exception as e:
            # Log error but don't fail the submission
            print(f"Email sending failed: {e}")
            return JsonResponse({
                'success': False,
                'message': "We couldn't send your message right now. Please try again later or contact me directly by email."
            }, status=500)
        
        return JsonResponse({
            'success': True,
            'message': 'Thank you for your message! I will get back to you soon.'
        })
    else:
        return JsonResponse({
            'success': False,
            'message': 'Please correct the errors below.',
            'errors': form.errors
        }, status=400)


def custom_404(request, exception):
    """Custom 404 error page."""
    return render(request, '404.html', status=404)


def custom_500(request):
    """Custom 500 error page."""
    return render(request, '500.html', status=500)
