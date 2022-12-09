from django import forms
 
class RecetaFormulario(forms.Form):
    usuario = forms.CharField()
    puntuacion = forms.IntegerField()
    comentario_breve=forms.CharField()
