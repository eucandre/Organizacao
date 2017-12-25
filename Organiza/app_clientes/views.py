from django.shortcuts import render

def Cria_segmento(request):
	if request.method == 'POST':
		form = FormSegmento(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = FormSegmento()
	return render(request,"Cria_segmento.html",{"form":form})


def Cria_Cliente(request):
	if request.method == 'POST':
		form = FormCliente(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = FormCliente()
	return render(request,"Cria_cliente.html",{"form":form})

