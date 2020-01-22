from django import forms

# Create your forms here.
class ToolsForm(forms.Form):

    sturlpath = forms.CharField(
        label='sturlpath',
        max_length=2083,
        required=True,
        widget=forms.TextInput(attrs={'class': "form-control"}),

    )

    fileExtension = forms.CharField(
        label='fileExtension',
        max_length=999,
        required=True,
        widget=forms.TextInput(attrs={'class': "form-control"}),

    )

    msg = forms.CharField(
        label='msg',
        required=False,
        widget=forms.Textarea(attrs={'class': "form-control",'readonly': 'true','rows':3,}),
    )
