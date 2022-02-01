from socket import fromshare
from django.forms import ModelForm
from .models import Information

class TaskForm(ModelForm):

    class Meta:
        model = Information
        fields = ('author', 'title', 'type', 'status', 'assignee', 'time_spent', 'description',)