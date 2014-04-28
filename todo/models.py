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
    """Fecha de creación del Proyecto"""
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


"""Clase Fase, define los campos y textos que contienen los datos de cada Fase"""


class Fase(models.Model):
    """
    Clase Fase
    Definimos los atributos de la clase Fase
    """
    fkproyecto = models.ForeignKey(Proyecto)
    """Nombre del Proyecto"""
    Nombre = models.CharField('Nombre', max_length=45, help_text='Ingrese el nombre de la fase')
    """Nombre de la Fase"""
    NroOrden = models.IntegerField(help_text='Ingrese el numero de orden de la fase')
    """Numero de orden de la Fase"""
    Descripcion = models.CharField('Descripcion', max_length=45, help_text='Ingrese la descripcion de la fase')
    """Descripción de la Fase"""
    FechaCreacion = models.DateField('Fecha de Creacion', help_text='Ingrese la fecha de creacion de la fase')
    """Fecha de creación de la Fase"""
    FechaInicio = models.DateField('Fecha de Inicio', help_text='Ingrese la fecha de Inicio de la fase', null=True,
                                   blank=True)
    """Fecha de inicio de la Fase"""
    FechaFin = models.DateField('Fecha de Fin', help_text='Ingrese la fecha de Fin de la fase', null=True, blank=True)
    """Fecha de finalizaciónde la Fase"""
    Estado = models.CharField('Estado', max_length=45, help_text='Ingrese el Estado de la fase', null=True, blank=True)
    """Estado de la Fase"""

    def __unicode__(self):
        return u'%s | %s' % (self.fkproyecto, self.Nombre)

    class Meta:
        """En esta clase definimos que se listaran las fases ordenados por el nombre"""
        ordering = ('Nombre',)
        verbose_name = u'Fase'
        verbose_name_plural = 'Fases'


class TipoItem(models.Model):
    """
    Clase TipoItem
    Definimos los atributos de la clase TipoItem
    """
    Fase = models.ForeignKey(Fase)
    Nombre = models.CharField('Nombre', max_length=45, help_text='Ingrese el nombre del Tipo de Item')
    """Nombre del Tipo de Item"""
    Descripcion = models.CharField('Descripcion', max_length=45,
                                   help_text='Ingrese la descripcion del del Tipo de Item')
    """Descripción del Tipo de Item"""

    def __unicode__(self):
        return u'%s | %s' % (self.Fase, self.Nombre)

    class Meta:
        """En esta clase definimos que se listaran los Tipos de Item por el nombre"""
        ordering = ('Nombre',)
        verbose_name = u'TipoItem'
        verbose_name_plural = 'Tipos de Item'


"""Clase Item, define los campos y textos que contienen los datos de cada Item"""


class Item(models.Model):
    """
    Clase Item
    Definimos los atributos de la clase Item
    """
    TipoItem = models.ForeignKey(TipoItem)
    """Nombre del TipoItem"""
    Nombre = models.CharField('Nombre', max_length=45, help_text='Ingrese el nombre de la Item')
    """Nombre del Item"""
    Descripcion = models.CharField('Descripcion', max_length=45, help_text='Ingrese la descripcion del Item')
    """Descripción del Item"""
    Complejidad = models.IntegerField(help_text='Ingrese la complejidad del Item')
    """Complejidad del Item"""
    Estado = models.CharField('Estado', max_length=45, help_text='Ingrese el Estado del Item', null=True, blank=True)
    """Estado del Item"""
    Version = models.IntegerField(help_text='Ingrese la Version del Item')
    """Version del Item"""
    Costo = models.IntegerField(help_text='Ingrese el costo del Item')
    """Costo del Item"""
    FechaModificacion = models.DateField('Fecha de Modificacion', help_text='Ingrese la fecha de modificacion del Item')
    """Fecha de modificacion del Item"""

    def __unicode__(self):
        return u'%s | %s' % (self.TipoItem, self.Nombre)

    class Meta:
        """En esta clase definimos que se listaran los Item ordenados por el nombre"""
        ordering = ('Nombre',)
        verbose_name = u'Item'
        verbose_name_plural = 'Items'


class RelacionItem(models.Model):
    """
    Clase RelacionItem
    Definimos los atributos de la clase RelacionItem
    """
    Item = models.ForeignKey(Item)
    """Nombre del Item1"""
    Descripcion = models.CharField('Descripcion', max_length=45, help_text='Ingrese la descripcion del Item')
    """Descripción del Item"""

    def __unicode__(self):
        return self.Nombre

    class Meta:
        """En esta clase definimos que se listaran las relaciones de los Item ordenados por el nombre"""
        ordering = ('Nombre',)
        verbose_name = u'RelacionItem'
        verbose_name_plural = 'Relacion Items'