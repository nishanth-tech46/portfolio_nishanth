"""
Admin configuration for the portfolio.
"""
from django.contrib import admin
from .models import Project, Certification, Skill, ContactMessage


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """Admin interface for Project model."""
    list_display = ['title', 'featured', 'created_at']
    list_filter = ['featured', 'created_at']
    search_fields = ['title', 'description', 'technologies']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['featured']


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    """Admin interface for Certification model."""
    list_display = ['name', 'issuer', 'issued_date']
    list_filter = ['issued_date']
    search_fields = ['name', 'issuer']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    """Admin interface for Skill model."""
    list_display = ['name', 'category', 'order']
    list_filter = ['category']
    list_editable = ['order']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    """Admin interface for ContactMessage model."""
    list_display = ['name', 'email', 'subject', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    readonly_fields = ['created_at']
