from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


FORM_INPUT_CLASSES = (
    "w-full rounded-2xl border border-white/10 bg-slate-950/80 px-4 py-3 "
    "text-sm text-white outline-none transition placeholder:text-slate-500 "
    "focus:border-cyan-400"
)


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter your username",
                "class": FORM_INPUT_CLASSES,
            }
        ),
    )

    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Enter your password",
                "class": FORM_INPUT_CLASSES,
            }
        ),
    )


class SignupForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="Email",
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Enter your email address",
                "class": FORM_INPUT_CLASSES,
            }
        ),
    )

    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Choose a username",
                "class": FORM_INPUT_CLASSES,
            }
        ),
    )

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Create a password",
                "class": FORM_INPUT_CLASSES,
            }
        ),
    )

    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Repeat your password",
                "class": FORM_INPUT_CLASSES,
            }
        ),
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with this email already exists.")

        return email