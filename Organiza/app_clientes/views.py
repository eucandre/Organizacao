from django.shortcuts import render
from .forms import *
from django.contrib import messages

def Cria_segmento(request):
	if request.method == 'POST':
		form = FormSegmento(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = FormSegmento()
	return render(request,"clientes/Cria_segmento.html",{"form":form})


def Cria_Cliente(request):
	if request.method == 'POST':
		form = FormCliente(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, 'Cliente Salvo!')
	else:
		form = FormCliente()
	return render(request,"clientes/Cria_cliente.html",{"form":form})

