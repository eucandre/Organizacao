from django import forms
from .models import *

DIAS = ((u'Segunda-feira','Segunda-feira'), (u'Terca-feira','Terca-feira'), (u'Quarta-feira','Quarta-feira'), (u'Quinta-feira','Quinta-feira')
        , (u'Sexta-feira','Sexta-feira'), (u'Sabado','Sabado'))

PERIODO= ((u'Manha', 'Manha'), (u'Tarde', 'Tarde'), (u'Manha e Tarde','Manha_e_Tarde'))



class FormDias(forms.ModelForm):
	dia = forms.ChoiceField(label='Dia',choices=DIAS, widget=forms.Select(attrs={"class":"form-control"}))
	class Meta:
		model = Dias
		fields = ('dia',)

class FormLideres(forms.ModelForm):
	lideres = forms.ModelMultipleChoiceField(label="Lideres",queryset=User.objects.all() ,widget=forms.SelectMultiple(attrs={"class":"form-control"}))

	class Meta:
		model = Lideres
		fields = ('lideres',)

class FormPromotores(forms.ModelForm):
	promotores = forms.ModelMultipleChoiceField(label="Promotores",queryset=User.objects.all(), widget=forms.SelectMultiple(attrs={"class":"form-control"}))

	class Meta:
		model = Lideres
		fields = ('promotores',)

class FormEquipe(forms.ModelForm):
	
	nome = forms.CharField(label='Nome',max_length = 150, widget=forms.TextInput(attrs={"class":"form-control"}))
	lideres = forms.ModelMultipleChoiceField(label="Lideres", queryset=Lideres.objects.all(), widget=forms.SelectMultiple(attrs={"class":"form-control"}))
	promotores = forms.ModelMultipleChoiceField(label="Promotores", queryset=Promotores.objects.all(), widget=forms.SelectMultiple(attrs={"class":"form-control"}))
	
	class Meta:
		model = Equipe
		fields =('nome', 'lideres', 'promotores')