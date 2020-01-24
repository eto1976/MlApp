from django import forms

# Create your forms here.
class IndexForm(forms.Form):

    username = forms.CharField(
        label='inputText',
        max_length=5,
        required=False,
        widget=forms.TextInput(attrs={'class': "form-control",'placeholder':'Id'}),
    )

    password = forms.CharField(
        label='inputPassword',
        max_length=20,
        required=False,
        widget=forms.PasswordInput(attrs={'class': "form-control",'placeholder':'Password'}),
    )

    msg = forms.CharField(
        label='msg',
        required=False,
    )
