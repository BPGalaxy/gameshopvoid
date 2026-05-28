from django import forms

class UserRegisterForm(forms.Form):
    Username = forms.CharField(label="Username", required=False, widget=forms.TextInput(attrs={"required":True}))
    First_name = forms.CharField(label="FirstName", required=False, widget=forms.TextInput(attrs={"required":True}))
    Last_name = forms.CharField(label="LastName", required=False, widget=forms.TextInput(attrs={"required":True}))
    Email = forms.EmailField(label="Email", required=False, widget=forms.TextInput(attrs={"required":True}))
    Password = forms.CharField(label="Password", required=False, widget=forms.PasswordInput(attrs={"required":True}))

class UserLoginForm(forms.Form):
    Username = forms.CharField(label="Username", required=False, widget=forms.TextInput(attrs={"required":True}))
    Password = forms.CharField(label="Password", required=False, widget=forms.PasswordInput(attrs={"required":True}))