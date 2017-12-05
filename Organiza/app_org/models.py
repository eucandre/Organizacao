# coding=utf-8
from __future__ import unicode_literals

from django.db import models
#As estruturas de banco de dados são determinadas aqui

class Perfil(models.Model):
    '''Estrutura de criação de perfil para usuários'''
    nome= models.CharField(max_length=150)

    def __unicode__(self):
        return self.nome

class Organizacional(models.Model):
    '''Estrutura de criação de organização'''
    nome = models.CharField(max_length=150)

    def __unicode__(self):
        return self.nome


class Unidade_comercial(models.Model):
    '''Estrutura de criação de unidade comercial'''
    nome = models.CharField(max_length=150)
    organizacao = models.ForeignKey(Organizacional)

    def __unicode__(self):
        return self.nome

class Marca(models.Model):
    '''Criação de marca'''
    nome = models.CharField(max_length=150)
    und_comerc = models.ForeignKey(Unidade_comercial)

    def __unicode__(self):
        return self.nome

class Regional(models.Model):
    '''Criação de setor regional'''
    nome = models.CharField(max_length=150)
    organizacao = models.ForeignKey(Organizacional)

    def __unicode__(self):
        return self.nome

class Colaborador(models.Model):
    '''Criaçãode colaborador'''
    nome = models.CharField(max_length=150)
    regiao = models.ForeignKey(Regional)

    def __unicode__(self):
        return self.nome

class Linhas_Produto(models.Model):
    '''Criação de linhas de produtos'''
    nome = models.CharField(max_length=150)
    marca= models.ForeignKey(Marca)

    def __unicode__(self):
        return self.nome

class Produto(models.Model):
    '''Criação de produtos'''
    nome = models.CharField(max_length=150)
    linha_produto = models.ForeignKey(Linhas_Produto)
    def __unicode__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    endereco = models.CharField(max_length=300)

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Clientes'




