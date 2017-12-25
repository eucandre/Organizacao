from __future__ import unicode_literals

from django.db import models
from app_usuario.models import *

PORTE = ((u'Pequeno','Pequeno'),(u'Medio','Medio'),(u'Grande','Grande'))

class Segmento(models.Model):
	nome = models.CharField(max_length=150)

	def __unicode__(self):
		return self.nome
	class Meta:
		verbose_name_plural = "Segmento a que se enquadra o cliente"

class Cliente(models.Model):

	nome_fantasia = models.CharField(max_length = 150)		
	cpf_cnpj = models.CharField(max_length=23)
	porte = models.CharField(max_length=8, choices=PORTE)
	segmento = models.ForeignKey(Segmento)
	email = models.EmailField()
	contato = models.CharField(max_length=150)
	cargo_contato = models.CharField(max_length=150)
	endereco = models.CharField(max_length=150)
	imagem_loja = models.ImageField()
	observacao = models.TextField()
	colaborador = models.ForeignKey(User)

	def __unicode__(self):
		return self.nome_fantasia

	class Meta:
		verbose_name_plural = "Clientes atendidos por colaboradores"

class Grupo_Clientes(models.Model):

	nome_grupo = models.CharField(max_length=150)
	clientes = models.ManyToManyField(Cliente)

	def __unicode__(self):
		return self.nome_grupo

	class Meta:
		verbose_name_plural = "Grupo de Clientes atendidos"
		