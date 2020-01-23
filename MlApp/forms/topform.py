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

    CHOICES_1 = [
        ('1', '学習処理'),
        ('2', '判別処理'),
        ('3', '学習データ削除'),
    ]

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

    exOp = forms.ChoiceField(
        label='exOp',
        required=False,
        widget=forms.RadioSelect, choices= CHOICES_1, initial=1
    )

    msg = forms.CharField(
        label='msg',
        required=False,
        widget=forms.Textarea(attrs={'class': "form-control",'readonly': 'true','rows':3,}),
    )

