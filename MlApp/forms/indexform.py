from django import forms

# Create your forms here.
class IndexForm(forms.Form):

    username = forms.CharField(
        label='Id',
        max_length=5,
        required=True,
    )

    password = forms.CharField(
        label='Password',
        max_length=20,
        required=True,
    )
