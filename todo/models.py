# -*- coding: utf-8 -*-
import datetime

from django.db import models





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
                                   editable=False, blank=True)
    """Fecha de inicio del Proyecto"""
    FechaFin = models.DateField('Fecha de Fin', help_text='Ingrese la fecha de Fin del proyecto', null=True, blank=True,
                                editable=False)
    """Fecha de finalización del Proyecto"""
    Estado_CHOICES = (
        ('I', 'Inactivo'),
        ('A', 'Iniciado/Activo'),
        ('T', 'Terminado'),
    )
    Estado = models.CharField('Estado', max_length=1, choices=Estado_CHOICES,
                              help_text='Ingrese el Estado del proyecto', null=True,
                              blank=True, default='I')
    """Estado del Proyecto"""

    def iniciar(self):
        self.FechaInicio = datetime.datetime.now()

    def __unicode__(self):
        """En esta clase definimos como se vera a la instancia de la clase Proyecto"""
        return self.Nombre


    class Meta:
        """En esta clase definimos que se listaran los proyectos ordenados por el nombre"""
        ordering = ('Nombre',)
        permissions = (
            ("ver proyecto", "Puede visualizar el proyecto"),
            ("iniciar proyecto", "Puede iniciar el proyecto"),
            ("administrar proyecto designadoo", "Puede administrar el proyecto que le fue designado"),
        )



class Fase(models.Model):
    """
    Clase Fase
    Definimos los atributos de la clase Fase
    """
    fkproyecto = models.ForeignKey(Proyecto, verbose_name="Proyecto", help_text='Seleccione el proyecto')
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
    Estado_CHOICES = (
        ('I', 'Inicio'),
        ('D', 'Desarrollo'),
        ('F', 'Finalizada'),
    )
    Estado = models.CharField('Estado', max_length=1, choices=Estado_CHOICES, help_text='Ingrese el Estado la Fase',
                              null=True,
                              blank=True, default='I')
    """Estado de la Fase"""

    def __unicode__(self):
        """En esta clase definimos como se vera a la instancia de la clase Fase"""
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
    Fase = models.ForeignKey(Fase, verbose_name="Fase", help_text='Seleccione la Fase')
    """Nombre de la Fase"""
    Nombre = models.CharField('Nombre', max_length=45, help_text='Ingrese el nombre del Tipo de Item')
    """Nombre del Tipo de Item"""
    Descripcion = models.CharField('Descripcion', max_length=45,
                                   help_text='Ingrese la descripcion del Tipo de Item')
    """Descripción del Tipo de Item"""

    def __unicode__(self):
        """En esta clase definimos como se vera a la instancia de la clase TipoItem"""
        return u'%s | %s' % (self.Fase, self.Nombre)

    class Meta:
        """En esta clase definimos que se listaran los Tipos de Item por el nombre"""
        ordering = ('Nombre',)
        verbose_name = u'TipoItem'
        verbose_name_plural = 'Tipos de Item'


class AtributoTipoItem(models.Model):
    """
    Clase AtributoTipoItem
    Definimos los atributos de la clase AtributoTipoItem
    """
    TipoItem = models.ForeignKey(TipoItem, verbose_name="Tipo de Item", help_text='Seleccione el Tipo de Item')
    """Nombre del Tipo de Item"""
    Nombre = models.CharField('Nombre', max_length=45, help_text='Ingrese el nombre del atributo del Tipo de Item')
    """Nombre del atributo del Tipo de Item"""
    Descripcion = models.CharField('Descripcion', max_length=45,
                                   help_text='Ingrese la descripcion del atributo del Tipo de Item')
    """Descripción del atributo del Tipo de Item"""

    def __unicode__(self):
        """En esta clase definimos como se vera a la instancia de la clase AtributoTipoItem"""
        return u'%s | %s' % (self.TipoItem, self.Nombre)

    class Meta:
        """En esta clase definimos que se listaran los Atributos del Tipos de Item por el nombre"""
        ordering = ('Nombre',)
        verbose_name = u'Atributo del Tipo Item'
        verbose_name_plural = 'Atributos del Tipo de Item'


class LineaBase(models.Model):
    """
    Clase LineaBase
    Definimos los atributos de la clase LineaBase
    """
    Fase = models.ForeignKey(Fase, verbose_name="Fase", help_text='Seleccione la Fase')
    """Nombre de la Fase"""
    Nombre = models.CharField('Nombre', max_length=45, help_text='Ingrese el nombre de la Linea Base')
    """Nombre de la Linea Base"""
    FechaCreacion = models.DateField('Fecha de Creacion', help_text='Ingrese la fecha de creacion de la Linea Base')
    """Fecha de creación de la Linea Base"""
    Estado_CHOICES = (
        ('I', 'Inicida'),
        ('A', 'Aprovada'),
    )
    Estado = models.CharField('Estado', max_length=1, choices=Estado_CHOICES,
                              help_text='Ingrese el Estado la Linea Base',
                              null=True,
                              blank=True, default='I')
    """Estado de la Linea Base"""

    def __unicode__(self):
        """En esta clase definimos como se vera a la instancia de la clase LineaBase"""
        return u'%s' % (self.Nombre)

    class Meta:
        """En esta clase definimos que se listaran las fases ordenados por el nombre"""
        ordering = ('Nombre',)
        verbose_name = u'Linea Base'
        verbose_name_plural = 'Lineas Base'


class Item(models.Model):
    """
    Clase Item
    Definimos los atributos de la clase Item
    """
    TipoItem = models.ForeignKey(TipoItem, verbose_name="Tipo de Item", help_text='Seleccione el tipo de Item')
    """Nombre del TipoItem"""
    LineaBase = models.ForeignKey(LineaBase, verbose_name="Linea Base", help_text='Seleccione la Linea Base', null=True,
                                  blank=True)
    """Nombre de la Linea Base"""
    Nombre = models.CharField('Nombre', max_length=45, help_text='Ingrese el nombre de la Item')
    """Nombre del Item"""
    Descripcion = models.CharField('Descripcion', max_length=45, help_text='Ingrese la descripcion del Item')
    """Descripción del Item"""
    Complejidad = models.IntegerField(help_text='Ingrese la complejidad del Item')
    """Complejidad del Item"""
    Estado_CHOICES = (
        ('M', 'En Modificacion'),
        ('P', 'Pendiente'),
        ('A', 'Aprobado'),
        ('R', 'Rechazado'),
        ('E', 'Eliminado'),
        ('V', 'En revision'),
    )
    Estado = models.CharField('Estado', max_length=1, choices=Estado_CHOICES, help_text='Ingrese el Estado del Item',
                              null=True,
                              blank=True, default='M')
    """Estado del Item"""
    Version = models.IntegerField(help_text='Ingrese la Version del Item')
    """Version del Item"""
    Costo = models.IntegerField(help_text='Ingrese el costo del Item')
    """Costo del Item"""
    FechaModificacion = models.DateField('Fecha de Modificacion', help_text='Ingrese la fecha de modificacion del Item')
    """Fecha de modificacion del Item"""

    def __unicode__(self):
        """En esta clase definimos como se vera a la instancia de la clase Item"""
        return u'%s | %s' % (self.TipoItem, self.Nombre)

    class Meta:
        """En esta clase definimos que se listaran los Item ordenados por el nombre"""
        ordering = ('Nombre',)
        verbose_name = u'Item'
        verbose_name_plural = 'Items'


class AtributoItem(models.Model):
    """
    Clase AtributoItem
    Definimos los atributos de la clase AtributoItem
    """
    Item = models.ForeignKey(Item, verbose_name="Item", help_text='Seleccione el  Item')
    """Nombre del Item"""
    AtributoTipoItem = models.ForeignKey(AtributoTipoItem, verbose_name="Atributo del Tipo de Item",
                                         help_text='Seleccione el  Atributo del Tipo de Item')
    """Nombre del Atributo del Tipo de Item"""
    Nombre = models.CharField('Nombre', max_length=45, help_text='Ingrese el nombre del atributo del Item')
    """Nombre del atributo del Item"""
    Descripcion = models.CharField('Descripcion', max_length=45,
                                   help_text='Ingrese la descripcion del atributo del Item')
    """Descripción del atributo del Item"""

    def __unicode__(self):
        """En esta clase definimos como se vera a la instancia de la clase AtributoItem"""
        return u'%s | %s' % (self.Item, self.Nombre)

    class Meta:
        """En esta clase definimos que se listaran los Atributos del Item por el nombre"""
        ordering = ('Nombre',)
        verbose_name = u'Atributo del Item'
        verbose_name_plural = 'Atributos del Item'


class RelacionItem(models.Model):
    """
    Clase RelacionItem
    Definimos los atributos de la clase RelacionItem
    """
    ItemOrigen = models.ForeignKey(Item, verbose_name="Item Origen", help_text='Seleccione el primer Item Origen',
                                   related_name="ItemOrigen")
    """Nombre del Item Origen"""

    TipoRelacion_CHOICES = (
        ('P', 'Pade - Hijo'),
        ('A', 'Antecesor - Sucesor'),
    )
    TipoRelacion = models.CharField('Tipo de Relacion', max_length=1, choices=TipoRelacion_CHOICES,
                                    help_text='Ingrese el Tipo de Relacion de los Items')
    """Tipo de Relacion Item"""
    ItemDestino = models.ForeignKey(Item, verbose_name="Item Destino", help_text='Seleccione el Item Destino',
                                    related_name="ItemDestino")
    """Nombre del Item Destino"""


    def __unicode__(self):
        """En esta clase definimos como se vera a la instancia de la clase RelacionItem"""
        return u'%s | %s | %s' % (self.ItemOrigen, self.TipoRelacion, self.ItemDestino)

    class Meta:
        """En esta clase definimos que se listaran las relaciones de los Item ordenados por el Item Origen"""
        ordering = ('ItemOrigen', 'ItemDestino',)
        verbose_name = u'Relacion Item'
        verbose_name_plural = 'Relacion Items'



