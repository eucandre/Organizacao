# coding=utf-8
from django import forms
from .models import *

class FormOrganizacao(forms.ModelForm):
    nome = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model= Organizacional
        fields= ('nome',)

class FormPerfil(forms.ModelForm):
    nome = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model= Perfil
        fields= ('nome',)

class FormUndComercial(forms.ModelForm):
    nome = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'form-control text-uppercase'}))
    organizacao = forms.ModelChoiceField(label='Organização',queryset=Organizacional.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))

    class Meta:
        model= Unidade_comercial
        fields= ('nome','organizacao')

class FormMarca(forms.ModelForm):
    nome = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'form-control'}))
    und_comerc = forms.ModelChoiceField(label='Unidade Comercial', queryset=Unidade_comercial.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))

    class Meta:
        model= Organizacional
        fields= ('nome','und_comerc')

class FormRegional(forms.ModelForm):
    nome = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'form-control'}))
    organizacao = forms.ModelChoiceField(label='Organização', queryset=Organizacional.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    class Meta:
        model= Organizacional
        fields= ('nome','organizacao')

class FormColaborador(forms.ModelForm):
    nome = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'form-control'}))
    regiao = forms.ModelChoiceField(label='Região', queryset= Regional.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    class Meta:
        model= Organizacional
        fields= ('nome','regiao')

class FormLinhaProduto(forms.ModelForm):
    nome = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'form-control'}))
    marca= forms.ModelChoiceField(queryset=Marca.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    class Meta:
        model= Organizacional
        fields= ('nome','marca')

class FormProduto(forms.ModelForm):
    nome = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'form-control'}))
    linha_produto = forms.ModelChoiceField(queryset=Linhas_Produto.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    class Meta:
        model= Organizacional
        fields= ('nome','linha_produto')

class FormCliente(forms.ModelForm):
    nome = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'form-control'}))
    endereco= forms.CharField(max_length=300, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model= Cliente
        fields = ('nome','endereco')