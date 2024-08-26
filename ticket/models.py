from django.db import models

# Create your models here.

class Ticket(models.Model):
    # iterable 
    possible_issues =( 
        ("1", "Missing results"), 
        ("2", "Biodata update"), 
        ("3", "Assault"), 
    )
    possible_status =( 
        ("1", "open"), 
        ("2", "close"), 
    )  
    category = models.CharField(max_length=255, choices=possible_issues)
    description = models.TextField()
    upload = models.ImageField(upload_to='upload/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.category} - {self.created_at}"



