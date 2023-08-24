from django.db import models


class Contato(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    celular = models.TextField(max_length=255)
    email = models.TextField(max_length=255)
    dtnasc = models.TextField(max_length=255)
