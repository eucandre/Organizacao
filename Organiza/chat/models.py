from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Conversa(models.Model):
	grupo  = models.ManyToManyField(User)
	mensagem = models.TextField()
	data  = models.DateField()
	hora = models.TimeField()

	def __unicode__(self):
		return self.grupo.__str__()

	class Meta:
		verbose_name_plural = "Grupo de conversa para o chat do sistema"
