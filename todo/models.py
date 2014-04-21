# -*- coding: utf-8 -*-
from django.db import models

#hola5


# Create your models here.

class Proyecto(models.Model):
    #Clase Proyecto
    #definimos los atributos de la clase Proyecto
    Nombre = models.CharField('Nombre', max_length=45, help_text='Ingrese el nombre del proyecto')
    Descripcion = models.CharField('Descripcion', max_length=45, help_text='Ingrese la descripcion del proyecto')
    FechaCreacion = models.DateField('Fecha de Creacion', help_text='Ingrese la fecha de creacion del proyecto')
    FechaInicio = models.DateField('Fecha de Inicio', help_text='Ingrese la fecha de Inicio del proyecto', null=True,
                                   blank=True)
    FechaFin = models.DateField('Fecha de Fin', help_text='Ingrese la fecha de Fin del proyecto', null=True, blank=True)
    Estado = models.CharField('Estado', max_length=45, help_text='Ingrese el Estado del proyecto', null=True,
                              blank=True)

    def __unicode__(self):
        return self.Nombre


    class Meta:
        #en esta clase definimos que se listaran los proyectos ordenados por el nombre
        ordering = ('Nombre',)
        permissions = (
            ("ver proyecto", "Puede visualizar el proyecto"),
            ("iniciar proyecto", "Puede iniciar el proyecto"),
        )


class Fase(models.Model):
    #Clase fase
    fkproyecto = models.ForeignKey(Proyecto)
    Nombre = models.CharField('Nombre', max_length=45, help_text='Ingrese el nombre de la fase')
    NroOrden = models.IntegerField(help_text='Ingrese el numero de orden de la fase')
    Descripcion = models.CharField('Descripcion', max_length=45, help_text='Ingrese la descripcion de la fase')
    FechaCreacion = models.DateField('Fecha de Creacion', help_text='Ingrese la fecha de creacion de la fase')
    FechaInicio = models.DateField('Fecha de Inicio', help_text='Ingrese la fecha de Inicio de la fase', null=True,
                                   blank=True)
    FechaFin = models.DateField('Fecha de Fin', help_text='Ingrese la fecha de Fin de la fase', null=True, blank=True)
    Estado = models.CharField('Estado', max_length=45, help_text='Ingrese el Estado de la fase', null=True, blank=True)

    def __unicode__(self):
        return u'%s | %s' % (self.fkproyecto, self.Nombre)

    class Meta:
        verbose_name = u'Fase'
        verbose_name_plural = 'Fases'

