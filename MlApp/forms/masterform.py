from django import forms

# Create your forms here.
class MasterForm(forms.Form):

    labelclass = forms.CharField(
        label='labelclass',
        max_length=3,
        required=False,
        widget=forms.TextInput(attrs={'class': "form-control"}),
    )

    labelclassname = forms.CharField(
        label='labelclassname',
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': "form-control"}),
    )

    baselabelclass = forms.CharField(
        label='baselabelclass',
        max_length=3,
        required=False,
        widget=forms.TextInput(attrs={'class': "form-control"}),
    )
