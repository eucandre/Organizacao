from django import forms

from .models import *

class FormConversa(forms.ModelForm):
	class Meta:
		model = Convesa
		fields = ('grupo','mensagem','data','hora')