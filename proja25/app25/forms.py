from django import forms

class StudentForms(forms.Form):
    file = forms.FileField()