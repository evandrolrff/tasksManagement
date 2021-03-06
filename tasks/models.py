from django.conf import settings
from django.db import models
from django.utils import timezone

class Publication(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

class Information(models.Model):
    TYPE_CHOICES = [
        ('B', 'Bug'),
        ('P', 'Phase'), 
        ('T', 'Task'), 
        ('U', 'User story')]
    TYPE_STATUS = [
        ('C', 'Closed'), 
        ('D', 'Developed'), 
        ('InP', 'In progress'), 
        ('InT', 'In testing'), 
        ('N', 'New'), 
        ('R', 'Rejected'), 
        ('S', 'Scheduled')]
    
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=255, choices=TYPE_CHOICES)
    status = models.CharField(max_length=255, choices=TYPE_STATUS)
    assignee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None , related_name='assignee')
    time_spent = models.DurationField(blank=True)
    description = models.TextField()
    discussion = models.ManyToManyField(Publication, blank=True)


    def __str__(self):
        return self.title
