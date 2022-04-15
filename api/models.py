from django.db import models

# Create your models here.
class Todo(models.Model):
    text = models.CharField(max_length=100)
    is_complete = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-updated']