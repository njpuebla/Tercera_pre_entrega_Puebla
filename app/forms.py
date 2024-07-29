from django import forms

class ElectricaFormulario(forms.Form):
    marca=forms.CharField(max_length=70)
    modelo=forms.CharField(max_length=70)
    
class AcusticaFormulario(forms.Form):
    marca=forms.CharField(max_length=70)
    modelo=forms.CharField(max_length=70)
    
class AmplificadoreFormulario(forms.Form):
    marca=forms.CharField(max_length=70)
    modelo=forms.CharField(max_length=70)

class EfectoFormulario(forms.Form):
    marca=forms.CharField(max_length=70)
    modelo=forms.CharField(max_length=70)