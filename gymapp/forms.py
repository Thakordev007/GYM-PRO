from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Contact


class RegisterForm(UserCreationForm):
    """Registration form with additional fields"""
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter email'
    }))
    mobile_number = forms.CharField(max_length=15, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter mobile number'
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'mobile_number', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter username'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter password'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirm password'
        })

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            # Save mobile number to profile
            if hasattr(user, 'profile'):
                user.profile.mobile_number = self.cleaned_data['mobile_number']
                user.profile.save()
            else:
                UserProfile.objects.create(user=user, mobile_number=self.cleaned_data['mobile_number'])
        return user


class ContactForm(forms.ModelForm):
    """Contact form"""
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Your full name',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'you@example.com',
                'required': True
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Tell us about your goals',
                'rows': 5,
                'required': True
            }),
        }

