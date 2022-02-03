from socket import fromshare
from django.forms import ModelForm, TextInput, TimeInput, Textarea, Select
from .models import Information
from django.contrib.auth.models import User

class TaskForm(ModelForm):

    class Meta:
        model = Information
        fields = ('author', 'title', 'type', 'status', 'assignee', 'time_spent', 'description',)
        widgets = {
            'author': Select(attrs={
                'class': "form-select",
                'style': '',
                }, choices=User.objects.all()),
            'title': TextInput(attrs={
                'class': "form-control",
                'style': '',
                'placeholder': 'Title'
                }),
            'type': Select(attrs={
                'class': "form-select",
                'style': ''
                }, choices=Information.TYPE_CHOICES),
            'status': Select(attrs={
                'class': "form-select",
                'style': ''
                }, choices=Information.TYPE_STATUS),
            'assignee': Select(attrs={
                'class': "form-select",
                'style': ''
                }, choices=User.objects.all()),
            'time_spent': TimeInput(attrs={
                'class': "form-control",
                'style': 'max-width: 100px;',
                'placeholder': "HH:mm"
                }),
            'description': Textarea(attrs={
                'class': "form-control",
                'style': '',
                'placeholder': 'Description'
                })
        }