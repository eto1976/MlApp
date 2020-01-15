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

#イメージラベルオブジェクト
imagelabel_ct1 = []
imagelabel_ct2 = []
imagelabel_ct3 = []

#カテゴリー1
CATEGORIES_1 = ()

for objimagelabel in Mst_imagelabel.objects.filter(baselabelclass__isnull=True):
    imagelabel_ct1.append(objimagelabel)

for imagelabel_ct1_obj in imagelabel_ct1:
    CATEGORIES_1_GET = (
        (imagelabel_ct1_obj.labelclass, imagelabel_ct1_obj.labelclassname),
    )

    CATEGORIES_1 = CATEGORIES_1 + CATEGORIES_1_GET

#カテゴリー2
CATEGORIES_2 = ()

for objimagelabel in Mst_imagelabel.objects.filter(baselabelclass='F01'):
    imagelabel_ct2.append(objimagelabel)

for imagelabel_ct2_obj in imagelabel_ct2:
    CATEGORIES_2_GET = (
        (imagelabel_ct2_obj.labelclass, imagelabel_ct2_obj.labelclassname),
    )

    CATEGORIES_2 = CATEGORIES_2 + CATEGORIES_2_GET

#カテゴリー3
CATEGORIES_3 = ()

for objimagelabel in Mst_imagelabel.objects.filter(baselabelclass='A01'):
    imagelabel_ct3.append(objimagelabel)

for imagelabel_ct3_obj in imagelabel_ct3:
    CATEGORIES_3_GET = (
        (imagelabel_ct3_obj.labelclass, imagelabel_ct3_obj.labelclassname),
    )

    CATEGORIES_3 = CATEGORIES_3 + CATEGORIES_3_GET


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
