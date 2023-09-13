from django import forms

class StudentForm(forms.Form):
    Sname=forms.CharField(max_length=10)
    Sid=forms.IntegerField()
    Sage=forms.IntegerField()
    Semail=forms.EmailField()
    