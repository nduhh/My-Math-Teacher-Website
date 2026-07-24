from django.db import models

class WaitingList(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    school = models.CharField(max_length=200, blank=True)
    grade = models.CharField(max_length=20, blank=True)
    province = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
    
class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject    
