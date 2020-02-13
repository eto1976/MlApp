from django import forms

# Create your forms here.
class ToolsForm(forms.Form):

    CHOICES_1 = [
        ('.jpg', 'jpg、jpeg'),
        ('.bmp', 'bmp'),
        ('.png', 'png'),
        ('.tiff', 'tiff'),
        ('.gif', 'gif'),
    ]

    stkeyword = forms.CharField(
        label='stkeyword',
        max_length=2083,
        required=True,
        widget=forms.TextInput(attrs={'class': "form-control"}),
    )

    sturlpath = forms.CharField(
        label='sturlpath',
        max_length=2083,
        required=True,
        widget=forms.TextInput(attrs={'class': "form-control",'readonly': 'readonly'}),
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
        widget=forms.Textarea(attrs={'class': "form-control",'readonly': 'true','rows':5,}),
    )
