from django import forms

# Create your forms here.
class ToolsForm(forms.Form):

    sturlpath = forms.CharField(
        label='sturlpath',
        max_length=2083,
        required=True,
    )

    fileExtension = forms.CharField(
        label='fileExtension',
        max_length=999,
        required=True,
    )

