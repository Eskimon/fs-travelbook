from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your forms here.


class NewUserForm(UserCreationForm):
    email = forms.EmailField(
        required=True, help_text="Required. Inform a valid email address."
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        blacklist = []
        with open("username-blacklist.txt") as f:
            blacklist = f.read().split()
        # check if in blacklist
        if username in blacklist:
            msg = "This username can not be used"
            self.add_error("username", msg)
