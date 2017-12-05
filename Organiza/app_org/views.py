from django.shortcuts import render
from .forms import *
from .models import *

def Apresentacao(request):
    return render(request,'index.html')

def Cria_Organizacao(request):
    if request.method == 'POST':
        form = FormOrganizacao(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = FormOrganizacao()
    return render(request,'Cria_Organizacao.html',{'form':form})

def Cria_Unidade_Comercial(request):
    if request.method == 'POST':
        form = FormUndComercial(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = FormUndComercial()
    return render(request,'Cria_Unidade_Comercial.html',{'form':form})


def Cria_Marca(request):
    if request.method == 'POST':
        form = FormMarca(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = FormMarca()
    return render(request,'Cria_Marca.html',{'form':form})

def Cria_Regional(request):
    if request.method == 'POST':
        form = FormRegional(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = FormRegional()
    return render(request,'Cria_Regional.html',{'form':form})

def Cria_Colaborador(request):
    if request.method == 'POST':
        form = FormColaborador(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = FormColaborador()
    return render(request,'Cria_Colaborador.html',{'form':form})

def Cria_Linha_Produto(request):
    if request.method == 'POST':
        form = FormLinhaProduto(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = FormLinhaProduto()
    return render(request,'Cria_Linha_Produto.html',{'form':form})

def Cria_Produto(request):
    if request.method == 'POST':
        form = FormProduto(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = FormProduto()
    return render(request,'Cria_Produto.html',{'form':form})

def Cria_Cliente(request):
    if request.method == 'POST':
        form = FormCliente(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = FormCliente()
    return render(request,'Cria_Cliente.html',{'form':form})

