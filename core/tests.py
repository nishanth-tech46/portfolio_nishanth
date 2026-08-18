"""
Tests for the portfolio application.
"""
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Project, Certification, Skill, ContactMessage
from .forms import ContactForm


class ProjectModelTest(TestCase):
    """Test cases for Project model."""
    
    def setUp(self):
        self.project = Project.objects.create(
            title='Test Project',
            description='A test project description',
            technologies='Python, Django',
            features='Feature 1, Feature 2',
            featured=True
        )
    
    def test_project_creation(self):
        """Test that a project can be created."""
        self.assertEqual(self.project.title, 'Test Project')
        self.assertTrue(self.project.featured)
        self.assertIsNotNone(self.project.slug)
    
    def test_project_slug_generation(self):
        """Test that slug is auto-generated from title."""
        self.assertEqual(self.project.slug, 'test-project')
    
    def test_get_technologies_list(self):
        """Test that technologies are split into a list."""
        tech_list = self.project.get_technologies_list()
        self.assertEqual(len(tech_list), 2)
        self.assertIn('Python', tech_list)
        self.assertIn('Django', tech_list)
    
    def test_get_features_list(self):
        """Test that features are split into a list."""
        feature_list = self.project.get_features_list()
        self.assertEqual(len(feature_list), 2)
        self.assertIn('Feature 1', feature_list)


class CertificationModelTest(TestCase):
    """Test cases for Certification model."""
    
    def setUp(self):
        self.certification = Certification.objects.create(
            name='Python Certification',
            issuer='Test Issuer',
            description='A test certification'
        )
    
    def test_certification_creation(self):
        """Test that a certification can be created."""
        self.assertEqual(self.certification.name, 'Python Certification')
        self.assertEqual(self.certification.issuer, 'Test Issuer')


class SkillModelTest(TestCase):
    """Test cases for Skill model."""
    
    def setUp(self):
        self.skill = Skill.objects.create(
            name='Python',
            category='programming',
            icon='code-2'
        )
    
    def test_skill_creation(self):
        """Test that a skill can be created."""
        self.assertEqual(self.skill.name, 'Python')
        self.assertEqual(self.skill.category, 'programming')


class ContactMessageModelTest(TestCase):
    """Test cases for ContactMessage model."""
    
    def setUp(self):
        self.message = ContactMessage.objects.create(
            name='John Doe',
            email='john@example.com',
            subject='Test Subject',
            message='Test message content'
        )
    
    def test_contact_message_creation(self):
        """Test that a contact message can be created."""
        self.assertEqual(self.message.name, 'John Doe')
        self.assertEqual(self.message.email, 'john@example.com')
        self.assertEqual(self.message.status, 'new')


class ContactFormTest(TestCase):
    """Test cases for ContactForm."""
    
    def test_valid_form(self):
        """Test that a valid form passes validation."""
        form_data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'subject': 'Test Subject',
            'message': 'This is a test message with enough characters.'
        }
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())
    
    def test_invalid_email(self):
        """Test that invalid email fails validation."""
        form_data = {
            'name': 'John Doe',
            'email': 'invalid-email',
            'subject': 'Test Subject',
            'message': 'This is a test message with enough characters.'
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())
    
    def test_short_message(self):
        """Test that short message fails validation."""
        form_data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'subject': 'Test Subject',
            'message': 'Short'
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())


class HomeViewTest(TestCase):
    """Test cases for home view."""
    
    def setUp(self):
        self.client = Client()
        self.project = Project.objects.create(
            title='Test Project',
            description='A test project',
            technologies='Python',
            featured=True
        )
        self.certification = Certification.objects.create(
            name='Test Cert',
            issuer='Test Issuer'
        )
        self.skill = Skill.objects.create(
            name='Python',
            category='programming'
        )
    
    def test_home_view_status_code(self):
        """Test that home view returns 200."""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
    
    def test_home_view_template(self):
        """Test that home view uses correct template."""
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')
    
    def test_home_view_context(self):
        """Test that home view sends correct context."""
        response = self.client.get(reverse('home'))
        self.assertIn('projects', response.context)
        self.assertIn('certifications', response.context)
        self.assertIn('skills', response.context)


class ProjectDetailViewTest(TestCase):
    """Test cases for project detail view."""
    
    def setUp(self):
        self.client = Client()
        self.project = Project.objects.create(
            title='Test Project',
            description='A test project',
            technologies='Python',
            slug='test-project'
        )
    
    def test_project_detail_view_status_code(self):
        """Test that project detail view returns 200."""
        response = self.client.get(reverse('project_detail', kwargs={'slug': 'test-project'}))
        self.assertEqual(response.status_code, 200)
    
    def test_project_detail_view_template(self):
        """Test that project detail view uses correct template."""
        response = self.client.get(reverse('project_detail', kwargs={'slug': 'test-project'}))
        self.assertTemplateUsed(response, 'project_detail.html')
    
    def test_project_detail_view_404(self):
        """Test that non-existent project returns 404."""
        response = self.client.get(reverse('project_detail', kwargs={'slug': 'non-existent'}))
        self.assertEqual(response.status_code, 404)


class ContactSubmitViewTest(TestCase):
    """Test cases for contact submit view."""
    
    def setUp(self):
        self.client = Client()
    
    def test_contact_submit_valid(self):
        """Test that valid contact form submission succeeds."""
        response = self.client.post(reverse('contact_submit'), {
            'name': 'John Doe',
            'email': 'john@example.com',
            'subject': 'Test Subject',
            'message': 'This is a test message with enough characters.'
        }, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(ContactMessage.objects.exists())
    
    def test_contact_submit_invalid(self):
        """Test that invalid contact form submission fails."""
        response = self.client.post(reverse('contact_submit'), {
            'name': 'John Doe',
            'email': 'invalid-email',
            'subject': 'Test Subject',
            'message': 'This is a test message with enough characters.'
        }, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 400)
    
    def test_contact_submit_get_method_not_allowed(self):
        """Test that GET method is not allowed for contact submit."""
        response = self.client.get(reverse('contact_submit'))
        self.assertEqual(response.status_code, 405)


class URLTest(TestCase):
    """Test cases for URL routing."""
    
    def test_home_url_resolves(self):
        """Test that home URL resolves correctly."""
        url = reverse('home')
        self.assertEqual(url, '/')
    
    def test_project_detail_url_resolves(self):
        """Test that project detail URL resolves correctly."""
        url = reverse('project_detail', kwargs={'slug': 'test-project'})
        self.assertEqual(url, '/project/test-project/')
    
    def test_contact_submit_url_resolves(self):
        """Test that contact submit URL resolves correctly."""
        url = reverse('contact_submit')
        self.assertEqual(url, '/contact/')
