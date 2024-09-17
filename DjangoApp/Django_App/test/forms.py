from django import forms

class TestForm(forms.Form):
    id = forms.IntegerField(label='ID')