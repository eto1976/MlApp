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

imagelabel_ct1 = []
imagelabel_ct2 = []
imagelabel_ct3 = []

#カテゴリー1
for objimagelabel in Mst_imagelabel.objects.filter(baselabelclass__isnull=True):
    imagelabel_ct1.append(objimagelabel)

CATEGORIES_1 = (
    (imagelabel_ct1[0].labelclass, imagelabel_ct1[0].labelclassname),
    (imagelabel_ct1[1].labelclass, imagelabel_ct1[1].labelclassname),
)

#カテゴリー2
for objimagelabel in Mst_imagelabel.objects.filter(baselabelclass='F01'):
    imagelabel_ct2.append(objimagelabel)

CATEGORIES_2 = (
    (imagelabel_ct2[0].labelclass, imagelabel_ct2[0].labelclassname),
)

#カテゴリー2

for objimagelabel in Mst_imagelabel.objects.filter(baselabelclass='A01'):
    imagelabel_ct3.append(objimagelabel)

CATEGORIES_3 = (
    (imagelabel_ct3[0].labelclass, imagelabel_ct3[0].labelclassname),
    (imagelabel_ct3[1].labelclass, imagelabel_ct3[1].labelclassname),
    (imagelabel_ct3[2].labelclass, imagelabel_ct3[2].labelclassname),
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
