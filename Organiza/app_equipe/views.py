from django.shortcuts import render

from .forms import *

def Cria_Dia(request):
	if request.method == "POST":
		form = FormDias(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = FormDias()

	return render(request, "equipe/cria_dia.html", {"form":form})

def Cria_lideres(request):
	if request.method == "POST":
		form = FormLideres(request.POST, request.FILES)
		if form.is_valid():
			form.save()
	else:
		form = FormLideres()

	return render(request, "equipe/cria_lideres.html", {"form":form})

def Cria_promotores(request):
	if request.method == "POST":
		form = FormPromotores(request.POST, request.FILES)
		if form.is_valid():
			form.save()
	else:
		form = FormPromotores()

	return render(request, "equipe/cria_promotores.html", {"form":form})

def Cria_equipe(request):
	if request.method == "POST":
		form = FormEquipe(request.POST, request.FILES)
		if form.is_valid():
			form.save()
	else:
		form = FormEquipe()

	return render(request, "equipe/cria_equipe.html", {"form":form})
