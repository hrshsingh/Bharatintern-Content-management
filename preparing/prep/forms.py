
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterFor(UserCreationForm):
    email=forms.EmailField(required=True)
    first_name=forms.CharField(max_length=50,required=True)
    last_name=forms.CharField(max_length=50,required=True)


    class Meta:
        model = User
        fields=('email','first_name','last_name','password1','password2')

    def save(self, commit=True):
        user=super(UserRegisterFor,self).save(commit=False)
        user.email=self.cleaned_data['email']
        user.first_name=self.cleaned_data['first_name']
        user.last_name=self.cleaned_data['last_name']
        user.username=self.cleaned_data['email']

        if commit:
            user.save()

        return user

