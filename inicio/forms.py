from django import forms

class FormularioCreacionGuitarra(forms.Form):
     marca = forms.CharField(max_length=20)
     modelo = forms.CharField(max_length=20)