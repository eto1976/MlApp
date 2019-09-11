from django import forms

# Create your forms here.
class TopForm(forms.Form):

    data = forms.CharField(
        label='data',
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
        max_length=999,
        required=True,
    )
