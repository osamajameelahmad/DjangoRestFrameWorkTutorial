from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.forms import ModelForm
from django.contrib.auth.forms import PasswordChangeForm
from core.models import CustomUser


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

    def clean(self):
        # print("clean")
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')


class SignUpForm(UserCreationForm):
    # name = forms.CharField(min_length=3, validators=[RegexValidator(r'^[a-zA-Z]+(([a-zA-Z ])?[a-zA-Z]*)*$')],
    #                        error_messages={'invalid': ("Not a valid Name")},
    #                        widget=forms.TextInput(
    #                            attrs={'class': 'form-control', 'placeholder': ''}), )
    email = forms.EmailField(min_length=3,
                             error_messages={'invalid': ("Not a valid email")},
                             widget=forms.TextInput(
                                 attrs={'class': 'form-control', 'placeholder': 'Email'}), )

    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'First Name'}), )
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Last Name'}), )
    image = forms.ImageField(label="Profile Picture")
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(label="Confirm Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))

    def clean(self):
        password = self.cleaned_data.get('password1')
        if len(str(password)) < 8:
            raise ValidationError('Password too short')

        mail = self.cleaned_data.get('email')
        user_obj = CustomUser.objects.filter(email__iexact=mail).first()
        if user_obj:
            msg = "Email Already Exists!"
            raise ValidationError(msg)
        else:
            return self.cleaned_data

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'image', 'password1', 'password2')