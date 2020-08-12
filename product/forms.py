from django import forms

class signupForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, required=True, help_text='Enter full name')
    phone = forms.CharField(label='Phone', max_length=15, required=True, help_text='Enter phone number')
    email = forms.EmailField(label='Email', max_length=250, required=True, help_text='Enter email')
    username = forms.CharField(label='Username', max_length=50, required=True, help_text='Enter username')
    password = forms.CharField(label='Password', max_length=50, widget=forms.PasswordInput, help_text='Enter password')

class loginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=250, required=True, help_text='Enter username')
    password = forms.CharField(label='Password', max_length=50, required=True, widget=forms.PasswordInput, help_text='Enter password')