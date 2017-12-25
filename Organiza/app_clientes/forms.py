from django import forms

from .models import *

class FormSegmento(forms.ModelForm):
	class Meta:
		model = Segmento
		fields = "__all__"