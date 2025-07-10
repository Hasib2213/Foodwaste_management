from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.label = ""  # remove label
            field.help_text = ""  # remove help text
            field.widget.attrs.update({
                'class': 'form-control mb-3',
                'placeholder': field_name.capitalize()
            })

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
