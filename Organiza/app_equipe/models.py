from __future__ import unicode_literals

from django.db import models

class Equipe(models.Model):
    nome= models.CharField(max_length=150)


