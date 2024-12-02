from django.db import models

class Carta (models.Model):
    """
        Modelo oque representa la estructura de datos
        de una carta de Yu-Gi-Oh! en base de datos
        """
    name = models.CharField('Nombre', max_length=50)
    type = models.CharField('Tipo', max_length=50)
    description = models.TextField('Descripción')
    race = models.CharField('Raza', max_length=50)
    attribute = models.CharField('Attribute', max_length=50)

    def __str__(self):
        return self.name
