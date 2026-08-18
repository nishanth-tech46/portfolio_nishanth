"""
Database models for the portfolio.
"""
from django.db import models
from django.core.validators import EmailValidator
from django.utils.text import slugify


class Project(models.Model):
    """Project model for portfolio projects."""
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    detailed_description = models.TextField(blank=True)
    technologies = models.CharField(max_length=500, help_text="Comma-separated list of technologies")
    features = models.TextField(blank=True, help_text="Comma-separated list of key features")
    github_repository = models.CharField(max_length=200, blank=True, help_text="GitHub repository name (e.g., e_learning_site)")
    github_url = models.URLField(blank=True, null=True)
    live_url = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-featured', 'order', '-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_technologies_list(self):
        return [tech.strip() for tech in self.technologies.split(',') if tech.strip()]

    def get_features_list(self):
        return [feature.strip() for feature in self.features.split(',') if feature.strip()]


class Certification(models.Model):
    """Certification model for professional certifications."""
    name = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    certificate_url = models.URLField(blank=True, null=True)
    issued_date = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ['-issued_date']

    def __str__(self):
        return f"{self.name} - {self.issuer}"


class Skill(models.Model):
    """Skill model for technical skills."""
    CATEGORY_CHOICES = [
        ('programming', 'Programming'),
        ('web', 'Web'),
        ('backend', 'Backend'),
        ('database', 'Database'),
        ('tools', 'Tools'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    icon = models.CharField(max_length=100, blank=True, help_text="Icon name from Lucide icons")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['category', 'order', 'name']

    def __str__(self):
        return self.name


class ContactMessage(models.Model):
    """Contact message model for form submissions."""
    name = models.CharField(max_length=100)
    email = models.EmailField(validators=[EmailValidator()])
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('new', 'New'),
            ('read', 'Read'),
            ('replied', 'Replied'),
        ],
        default='new'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.subject}"
