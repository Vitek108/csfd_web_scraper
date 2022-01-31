from django import forms


class SearchForm(forms.Form):
    q = forms.CharField(label="Hledat", max_length=50)