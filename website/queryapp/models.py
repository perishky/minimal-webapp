from django.db import models

class User(models.Model):
    """User model matching MySQL schema"""
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'users'
        managed = False  # Don't let Django manage this table
    
    def __str__(self):
        return self.name
