"""
Context processors for the portfolio application.
"""
from django.conf import settings


def social_links(request):
    """
    Context processor to make social links available in all templates.
    """
    return {
        'github_url': getattr(settings, 'GITHUB_URL', ''),
        'github_username': getattr(settings, 'GITHUB_USERNAME', ''),
        'linkedin_url': getattr(settings, 'LINKEDIN_URL', ''),
        'contact_email': getattr(settings, 'CONTACT_EMAIL', ''),
    }
