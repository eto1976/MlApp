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

    dataFolder = forms.CharField(
        label='dataFolder',
        max_length=260,
        required=True,
    )

    testFile = forms.CharField(
        label='testFile',
        max_length=260,
        required=True,
    )

    exOp = forms.CharField(
        label='exOp',
        max_length=1,
        required=True,
    )

    msg = forms.CharField(
        label='msg',
        required=True,
        widget=forms.Textarea,
    )

    category_1 = forms.ChoiceField(
        choices=EMPTY_CHOICES_1,
        widget=forms.Select(attrs={'class':'bootstrap-select','onchange': 'form.submit();'})
        )

    category_2 = forms.ChoiceField(
        choices=EMPTY_CHOICES_2,
        widget=forms.Select(attrs={'class':'bootstrap-select','onchange': 'form.submit();'})
        )

    category_3 = forms.ChoiceField(
        choices=EMPTY_CHOICES_3,
        widget=forms.Select(attrs={'class':'bootstrap-select'})
        )
