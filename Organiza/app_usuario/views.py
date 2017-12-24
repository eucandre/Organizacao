from django.shortcuts import render
from .forms import *

def Cria_usuario(request):
	if request.method == "POST":
		form = FormUser(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = FormUser()
	return render(request, "usuarios/cadastro_usuario.html",{"form":form})