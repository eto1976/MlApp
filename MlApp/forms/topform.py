from django import forms
from MlApp.models.mstimagelabel import Mst_imagelabel

# Create your forms here.

EMPTY_CHOICES_1 = (
    ('', '-----ラベル階層1-----'),
)
EMPTY_CHOICES_2 = (
    ('', '-----ラベル階層2-----'),
)
EMPTY_CHOICES_3 = (
    ('', '-----ラベル階層3-----'),
)

CATEGORIES_1 = (
    ('1', '果物'),
    ('2', '野菜'),
)

CATEGORIES_2 = (
    ('1', 'りんご'),
    ('2', 'みかん'),
)

CATEGORIES_3 = (
    ('1', 'りんご1等級'),
    ('2', 'りんご2等級'),
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

    category_1 = forms.ChoiceField(
        choices=EMPTY_CHOICES_1 + CATEGORIES_1,
        widget=forms.Select(attrs={'class':'bootstrap-select'}))

    category_2 = forms.ChoiceField(
        choices=EMPTY_CHOICES_2 + CATEGORIES_2,
        widget=forms.Select(attrs={'class':'bootstrap-select'}))

    category_3 = forms.ChoiceField(
        choices=EMPTY_CHOICES_3 + CATEGORIES_3,
        widget=forms.Select(attrs={'class':'bootstrap-select'}))
