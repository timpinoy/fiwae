from django import forms


class UploadTransactionForm(forms.Form):
    file = forms.FileField(label="KBC CSV")