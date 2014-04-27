# -*- coding: utf-8 -*-
from django.db import models

#hola5




"""Models contiene los modelos del proyecto"""


class Proyecto(models.Model):
    """
    Clase Proyecto
    Definimos los atributos de la clase Proyecto
    """

    Nombre = models.CharField('Nombre', max_length=45, help_text='Ingrese el nombre del proyecto')
    """Nombre del Proyecto"""
    Descripcion = models.CharField('Descripcion', max_length=45, help_text='Ingrese la descripcion del proyecto')
    """Descripción del Proyecto"""
    FechaCreacion = models.DateField('Fecha de Creacion', help_text='Ingrese la fecha de creacion del proyecto')
    """Descripción del Proyecto"""
    FechaInicio = models.DateField('Fecha de Inicio', help_text='Ingrese la fecha de Inicio del proyecto', null=True,
                                   blank=True)
    """Fecha de inicio del Proyecto"""
    FechaFin = models.DateField('Fecha de Fin', help_text='Ingrese la fecha de Fin del proyecto', null=True, blank=True)
    """Fecha de finalización del Proyecto"""
    Estado = models.CharField('Estado', max_length=45, help_text='Ingrese el Estado del proyecto', null=True,
                              blank=True)
    """Estado del Proyecto"""

    def __unicode__(self):
        return self.Nombre


    class Meta:
        """En esta clase definimos que se listaran los proyectos ordenados por el nombre"""
        ordering = ('Nombre',)
        permissions = (
            ("ver proyecto", "Puede visualizar el proyecto"),
            ("iniciar proyecto", "Puede iniciar el proyecto"),
            ("administrar proyecto designadoo", "Puede administrar el proyecto que le fue designado"),
        )

#Clase Fase, define los campos y textos que contienen los datos de cada Fase
class Fase(models.Model):
    """
    Clase Fase
    Definimos los atributos de la clase Fase
    """
    Proyecto = models.ForeignKey(Proyecto)
    Nombre = models.CharField('Nombre', max_length=45, help_text='Ingrese el nombre de la fase')
    NroOrden = models.IntegerField(help_text='Ingrese el numero de orden de la fase')
    Descripcion = models.CharField('Descripcion', max_length=45, help_text='Ingrese la descripcion de la fase')
    FechaCreacion = models.DateField('Fecha de Creacion', help_text='Ingrese la fecha de creacion de la fase')
    FechaInicio = models.DateField('Fecha de Inicio', help_text='Ingrese la fecha de Inicio de la fase', null=True,
                                   blank=True)
    FechaFin = models.DateField('Fecha de Fin', help_text='Ingrese la fecha de Fin de la fase', null=True, blank=True)
    Estado = models.CharField('Estado', max_length=45, help_text='Ingrese el Estado de la fase', null=True, blank=True)

    def __unicode__(self):
        return u'%s | %s' % (self.Proyecto, self.Nombre)

    class Meta:
        """En esta clase definimos que se listaran los proyectos ordenados por el nombre"""
        verbose_name = u'Fase'
        verbose_name_plural = 'Fases'

