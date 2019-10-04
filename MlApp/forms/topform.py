from django import forms

# Create your forms here.

CATEGORIES = (
    ('1', '果物'),
    ('2', '野菜'),
)

class TopForm(forms.Form):

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

    category = forms.ChoiceField(
        choices=CATEGORIES,
        widget=forms.Select(attrs={'class':'bootstrap-select'}))
