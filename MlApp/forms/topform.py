from django import forms

# Create your forms here.
class TopForm(forms.Form):

    EMPTY_CHOICES_1 = (
        ('', '-----ラベル階層1-----'),
    )
    EMPTY_CHOICES_2 = (
        ('', '-----ラベル階層2-----'),
    )
    EMPTY_CHOICES_3 = (
        ('', '-----ラベル階層3-----'),
    )

    category_1 = forms.ChoiceField(
        choices=EMPTY_CHOICES_1,
        required=False,
        widget=forms.Select(attrs={'class':'bootstrap-select','onchange': 'form.submit();'})
        )

    category_2 = forms.ChoiceField(
        choices=EMPTY_CHOICES_2,
        required=False,
        widget=forms.Select(attrs={'class':'bootstrap-select','onchange': 'form.submit();'})
        )

    category_3 = forms.ChoiceField(
        choices=EMPTY_CHOICES_3,
        required=False,
        widget=forms.Select(attrs={'class':'bootstrap-select'})
        )


    dataFolder = forms.CharField(
        label='dataFolder',
        max_length=260,
        required=False,
        widget=forms.TextInput(attrs={'class': "form-control"}),
    )

    testFile = forms.CharField(
        label='testFile',
        required=False,
        max_length=260,
    )

    exOp = forms.CharField(
        label='exOp',
        max_length=1,
        required=True,
    )

    msg = forms.CharField(
        label='msg',
        required=False,
        widget=forms.Textarea(attrs={'class': "form-control",'readonly': 'true','rows':4,}),
    )

