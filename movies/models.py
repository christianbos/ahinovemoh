from django.db import models


class Movies(models.Model):
    CINE_CHOICES = {
        ('cmxr', 'Cinemex Reforma')
        ('cmxc', 'Cinemex Coapa')
    }

    HORARIOS_CHOICES = {
        ('hr', ('13:00', '14:00', '20:00'))
        ('hc', ('15:00', '17:00', '22:00'))
    }

    titulo = models.CharField(max_length=100)
    cine = models.CharField(max_length=50, choices=CINE_CHOICES)
    horario = models.CharField(max_length=50, choices=HORARIOS_CHOICES)
    imagen = models.ImageField('upload_to=')
