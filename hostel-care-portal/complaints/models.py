from django.db import models
from django.contrib.auth.models import User

class Complaint(models.Model):
    # Category choices
    CATEGORY_CHOICES = [
        ('Electrical', 'Electrical'),
        ('Plumbing', 'Plumbing'),
        ('Furniture', 'Furniture'),
        ('Cleaning', 'Cleaning'),
        ('Other', 'Other'),
    ]

    # Status choices
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]

    # Fields
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Electrical')
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    
    # New image attachment field (optional)
    image = models.ImageField(upload_to='complaint_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.user.username}"