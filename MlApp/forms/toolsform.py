from django import forms

# Create your forms here.
class ToolsForm(forms.Form):

    CHOICES_1 = [
        ('1', 'jpg、jpeg'),
        ('2', 'bmp'),
        ('3', 'png'),
        ('4', 'tiff'),
        ('5', 'gif'),
    ]

    sturlpath = forms.CharField(
        label='sturlpath',
        max_length=2083,
        required=True,
        widget=forms.TextInput(attrs={'class': "form-control"}),

    )

    fileExtension = forms.MultipleChoiceField(
        label='fileExtension',
        choices=CHOICES_1,
        required=True,
        widget=forms.CheckboxSelectMultiple(attrs={'class': "checkbox-inline"}),
    )

    msg = forms.CharField(
        label='msg',
        required=False,
        widget=forms.Textarea(attrs={'class': "form-control",'readonly': 'true','rows':3,}),
    )
