from django import forms



class regform(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField()
    password = forms.CharField(max_length=30)
    password2 = forms.CharField(max_length=30)
    mobile = forms.IntegerField()
    address = forms.CharField(max_length=100)


class logform(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=30)