from __future__ import unicode_literals

from django.db import models

DIAS = ((u'Segunda-feira','Segunda-feira'), (u'Terca-feira','Terca-feira'), (u'Quarta-feira','Quarta-feira'), (u'Quinta-feira','Quinta-feira')
        , (u'Sexta-feira','Sexta-feira'), (u'Sabado','Sabado'))

PERIODO= ((u'Manha', 'Manha'), (u'Tarde', 'Tarde'), (u'Manha e Tarde','Manha_e_Tarde'))

class Dias(models.Model):
    dia = models.CharField(choices=DIAS,max_length=150)

    def __unicode__(self):
        return self.dia.__str__()

    class Meta:
        verbose_name_plural = 'Dias da semana de jornada'

class Jornada(models.Model):
    nome= models.CharField(max_length=150)
    dias_jornada =models.ForeignKey(Dias)
    periodo = models.CharField(choices=PERIODO, max_length=150)
    de = models.TimeField()
    ate = models.TimeField()

    def __unicode__(self):
        return self.nome.__str__()
