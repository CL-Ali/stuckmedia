from django.db import models

class ClientFeedback(models.Model):
    image = models.ImageField(upload_to='client_feedback_images/', blank=True, null=True)
    feedback = models.TextField()
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)

    def __str__(self):
        return f"Feedback from {self.name} - {self.designation}"

class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default='')  # Default empty string
    tags = models.JSONField()  # Stores a list of tags
    link = models.URLField()

    def __str__(self):
        return self.title

class PricingPlan(models.Model):
    service = models.ForeignKey(Service, related_name='pricing_plans', on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    price = models.CharField(max_length=50)
    includes = models.JSONField()  # Stores a list of features

    def __str__(self):
        return f"{self.type} - {self.service.name}"

class SkillCategory(models.Model):
    name = models.CharField(max_length=100)
    skills = models.JSONField()  # Stores a list of skills

    def __str__(self):
        return self.name

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team_member_images/', blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.role}"

