# -*- coding: utf-8 -*-
import datetime

from django.db import models





"""Models contiene los modelos del proyecto"""
class Proyecto(models.Model):
    """
    Clase Proyecto
    Definimos los atributos de la clase Proyecto
    """

    nombre = models.CharField('Nombre', max_length=45, help_text='Ingrese el nombre del proyecto')
    """Nombre del Proyecto"""
    descripcion = models.CharField('Descripcion', max_length=45, help_text='Ingrese la descripcion del proyecto')
    """Descripción del Proyecto"""
    fechacreacion = models.DateField('Fecha de Creacion', help_text='Ingrese la fecha de creacion del proyecto')
    """Fecha de creación del Proyecto"""
    fechainicio = models.DateField('Fecha de Inicio', help_text='Ingrese la fecha de Inicio del proyecto', null=True,
                                   editable=False, blank=True)
    """Fecha de inicio del Proyecto"""
    fechafin = models.DateField('Fecha de Fin', help_text='Ingrese la fecha de Fin del proyecto', null=True, blank=True,
                                editable=False)
    """Fecha de finalización del Proyecto"""
    Estado_CHOICES = (
        ('I', 'Inactivo'),
        ('A', 'Iniciado/Activo'),
        ('T', 'Terminado'),
    )
    estado = models.CharField('Estado', max_length=1, choices=Estado_CHOICES,
                              help_text='Ingrese el Estado del proyecto', null=True,
                              blank=True, default='I')
    """Estado del Proyecto"""

    def iniciar(self):
        self.fechainicio = datetime.datetime.now()

    def finalizar(self):
        self.fechafin = datetime.datetime.now()

    def __unicode__(self):
        """En esta clase definimos como se vera a la instancia de la clase Proyecto"""
        return self.nombre


    class Meta:
        """En esta clase definimos que se listaran los proyectos ordenados por el nombre"""
        ordering = ('nombre',)
        permissions = (
            ("ver_proyecto", "Puede visualizar el proyecto"),
            ("iniciar_proyecto", "Puede iniciar el proyecto"),
            ("administrar_proyecto_designado", "Puede administrar el proyecto que le fue designado"),
        )



class Fase(models.Model):
    """
    Clase Fase
    Definimos los atributos de la clase Fase
    """
    fkproyecto = models.ForeignKey(Proyecto, verbose_name="Proyecto", help_text='Seleccione el proyecto')
    """Nombre del Proyecto"""
    nombre = models.CharField('Nombre', max_length=45, help_text='Ingrese el nombre de la fase')
    """Nombre de la Fase"""
    nroorden = models.IntegerField(help_text='Ingrese el numero de orden de la fase')
    """Numero de orden de la Fase"""
    descripcion = models.CharField('Descripcion', max_length=45, help_text='Ingrese la descripcion de la fase')
    """Descripción de la Fase"""
    fechacreacion = models.DateField('Fecha de Creacion', help_text='Ingrese la fecha de creacion de la fase')
    """Fecha de creación de la Fase"""
    fechainicio = models.DateField('Fecha de Inicio', help_text='Ingrese la fecha de Inicio de la fase', null=True,
                                   blank=True)
    """Fecha de inicio de la Fase"""
    fechafin = models.DateField('Fecha de Fin', help_text='Ingrese la fecha de Fin de la fase', null=True, blank=True)
    """Fecha de finalizaciónde la Fase"""
    Estado_CHOICES = (
        ('I', 'Inicio'),
        ('D', 'Desarrollo'),
        ('F', 'Finalizada'),
    )
    estado = models.CharField('Estado', max_length=1, choices=Estado_CHOICES, help_text='Ingrese el Estado la Fase',
                              null=True,
                              blank=True, default='I')
    """Estado de la Fase"""

    def __unicode__(self):
        """En esta clase definimos como se vera a la instancia de la clase Fase"""
        return u'%s | %s' % (self.fkproyecto, self.nombre)

    class Meta:
        """En esta clase definimos que se listaran las fases ordenados por el nombre"""
        ordering = ('nombre',)
        verbose_name = u'Fase'
        verbose_name_plural = 'Fases'


class TipoItem(models.Model):
    """
    Clase TipoItem
    Definimos los atributos de la clase TipoItem
    """
    fase = models.ForeignKey(Fase, verbose_name="Fase", help_text='Seleccione la Fase')
    """Nombre de la Fase"""
    nombre = models.CharField('Nombre', max_length=45, help_text='Ingrese el nombre del Tipo de Item')
    """Nombre del Tipo de Item"""
    descripcion = models.CharField('Descripcion', max_length=45,
                                   help_text='Ingrese la descripcion del Tipo de Item')
    """Descripción del Tipo de Item"""

    def __unicode__(self):
        """En esta clase definimos como se vera a la instancia de la clase TipoItem"""
        return u'%s | %s' % (self.fase, self.nombre)

    class Meta:
        """En esta clase definimos que se listaran los Tipos de Item por el nombre"""
        ordering = ('nombre',)
        verbose_name = u'TipoItem'
        verbose_name_plural = 'Tipos de Item'


class AtributoTipoItem(models.Model):
    """
    Clase AtributoTipoItem
    Definimos los atributos de la clase AtributoTipoItem
    """
    tipoitem = models.ForeignKey(TipoItem, verbose_name="Tipo de Item", help_text='Seleccione el Tipo de Item')
    """Nombre del Tipo de Item"""
    nombre = models.CharField('Nombre', max_length=45, help_text='Ingrese el nombre del atributo del Tipo de Item')
    """Nombre del atributo del Tipo de Item"""
    descripcion = models.CharField('Descripcion', max_length=45,
                                   help_text='Ingrese la descripcion del atributo del Tipo de Item')
    """Descripción del atributo del Tipo de Item"""

    def __unicode__(self):
        """En esta clase definimos como se vera a la instancia de la clase AtributoTipoItem"""
        return u'%s | %s' % (self.tipoitem, self.nombre)

    class Meta:
        """En esta clase definimos que se listaran los Atributos del Tipos de Item por el nombre"""
        ordering = ('nombre',)
        verbose_name = u'Atributo del Tipo Item'
        verbose_name_plural = 'Atributos del Tipo de Item'


class LineaBase(models.Model):
    """
    Clase LineaBase
    Definimos los atributos de la clase LineaBase
    """
    fase = models.ForeignKey(Fase, verbose_name="Fase", help_text='Seleccione la Fase')
    """Nombre de la Fase"""
    nombre = models.CharField('Nombre', max_length=45, help_text='Ingrese el nombre de la Linea Base')
    """Nombre de la Linea Base"""
    fechacreacion = models.DateField('Fecha de Creacion', help_text='Ingrese la fecha de creacion de la Linea Base')
    """Fecha de creación de la Linea Base"""
    Estado_CHOICES = (
        ('I', 'Inicida'),
        ('A', 'Aprovada'),
    )
    estado = models.CharField('Estado', max_length=1, choices=Estado_CHOICES,
                              help_text='Ingrese el Estado la Linea Base',
                              null=True,
                              blank=True, default='I')
    """Estado de la Linea Base"""


    def __unicode__(self):
        """En esta clase definimos como se vera a la instancia de la clase LineaBase"""
        return u'%s' % (self.nombre)

    class Meta:
        """En esta clase definimos que se listaran las fases ordenados por el nombre"""
        ordering = ('nombre',)
        verbose_name = u'Linea Base'
        verbose_name_plural = 'Lineas Base'


class Item(models.Model):
    """
    Clase Item
    Definimos los atributos de la clase Item
    """
    tipoitem = models.ForeignKey(TipoItem, verbose_name="Tipo de Item", help_text='Seleccione el tipo de Item')
    """Nombre del TipoItem"""
    lineabase = models.ForeignKey(LineaBase, verbose_name="Linea Base", help_text='Seleccione la Linea Base', null=True,
                                  blank=True)
    """Nombre de la Linea Base"""
    nombre = models.CharField('Nombre', max_length=45, help_text='Ingrese el nombre de la Item')
    """Nombre del Item"""
    descripcion = models.CharField('Descripcion', max_length=45, help_text='Ingrese la descripcion del Item')
    """Descripción del Item"""
    complejidad = models.IntegerField(help_text='Ingrese la complejidad del Item')
    """Complejidad del Item"""
    costo = models.IntegerField(help_text='Ingrese el costo del Item en Dolares $')
    """Costo del Item"""
    Estado_CHOICES = (
        ('M', 'En Modificacion'),
        ('P', 'Pendiente'),
        ('A', 'Aprobado'),
        ('R', 'Rechazado'),
        ('E', 'Eliminado'),
        ('V', 'En revision'),
    )
    estado = models.CharField('Estado', max_length=1, choices=Estado_CHOICES, help_text='Ingrese el Estado del Item',
                              null=True,
                              blank=True, default='M')
    """Estado del Item"""
    version = models.IntegerField(help_text='Ingrese la Version del Item')
    """Version del Item"""
    fechamodificacion = models.DateField('Fecha de Modificacion', help_text='Ingrese la fecha de modificacion del Item')
    """Fecha de modificacion del Item"""
    complejidadtotal = models.IntegerField(null=True, blank=True, verbose_name="Complejidad total al modificar")
    """Complejidad del Item"""
    costototal = models.IntegerField(null=True, blank=True, verbose_name="Costo total al modificar")
    """Costo del Item"""
    idversion = models.IntegerField(null=True,
                                    blank=True, )
    """Id del de la version del Item"""

    def __unicode__(self):
        """En esta clase definimos como se vera a la instancia de la clase Item"""
        return u'%s | %s' % (self.tipoitem, self.nombre)

    class Meta:
        """En esta clase definimos que se listaran los Item ordenados por el nombre"""
        ordering = ('nombre',)
        verbose_name = u'Item'
        verbose_name_plural = 'Items'

    def save(self):
        existe = False
        existe = Item.objects.filter(id=self.id).exists()
        ols = Item.objects.filter(id=self.id)
        if existe is True:
            for ol in ols:
                if ol.idversion == self.idversion:
                    self.cambiarversion()
                    self.version = self.version + 1
        self.fechamodificacion = datetime.datetime.now()
        super(Item, self).save()
        return Item

    def cambiarversion(self):
        olds = Item.objects.filter(id=self.id)
        for old in olds:
            new = Item()
            new.nombre = old.nombre
            new.tipoitem = old.tipoitem
            new.lineabase = old.lineabase
            new.nombre = old.nombre
            new.descripcion = old.descripcion
            new.complejidad = old.complejidad
            new.costo = old.costo
            new.estado = old.estado
            new.version = old.version
            new.costototal = old.costototal
            new.complejidadtotal = old.complejidadtotal
            new.idversion = old.id
            new.save()
        return Item


class AtributoItem(models.Model):
    """
    Clase AtributoItem
    Definimos los atributos de la clase AtributoItem
    """
    item = models.ForeignKey(Item, verbose_name="Item", help_text='Seleccione el  Item')
    """Nombre del Item"""
    atributotipoitem = models.ForeignKey(AtributoTipoItem, verbose_name="Atributo del Tipo de Item",
                                         help_text='Seleccione el  Atributo del Tipo de Item')
    """Nombre del Atributo del Tipo de Item"""
    nombre = models.CharField('Nombre', max_length=45, help_text='Ingrese el nombre del atributo del Item')
    """Nombre del atributo del Item"""
    descripcion = models.CharField('Descripcion', max_length=45,
                                   help_text='Ingrese la descripcion del atributo del Item')
    """Descripción del atributo del Item"""

    def __unicode__(self):
        """En esta clase definimos como se vera a la instancia de la clase AtributoItem"""
        return u'%s | %s' % (self.item, self.nombre)

    class Meta:
        """En esta clase definimos que se listaran los Atributos del Item por el nombre"""
        ordering = ('nombre',)
        verbose_name = u'Atributo del Item'
        verbose_name_plural = 'Atributos del Item'


class RelacionItem(models.Model):
    """
    Clase RelacionItem
    Definimos los atributos de la clase RelacionItem
    """
    itemorigen = models.ForeignKey(Item, verbose_name="Item Origen", help_text='Seleccione el primer Item Origen',
                                   related_name="ItemOrigen")
    """Nombre del Item Origen"""

    TipoRelacion_CHOICES = (
        ('P', 'Pade - Hijo'),
        ('A', 'Antecesor - Sucesor'),
    )
    tiporelacion = models.CharField('Tipo de Relacion', max_length=1, choices=TipoRelacion_CHOICES,
                                    help_text='Ingrese el Tipo de Relacion de los Items')
    """Tipo de Relacion Item"""
    itemdestino = models.ForeignKey(Item, verbose_name="Item Destino", help_text='Seleccione el Item Destino',
                                    related_name="ItemDestino")
    """Nombre del Item Destino"""


    def __unicode__(self):
        """En esta clase definimos como se vera a la instancia de la clase RelacionItem"""
        return u'%s | %s | %s' % (self.itemorigen, self.tiporelacion, self.itemdestino)

    class Meta:
        """En esta clase definimos que se listaran las relaciones de los Item ordenados por el Item Origen"""
        ordering = ('itemorigen', 'itemdestino',)
        verbose_name = u'Relacion Item'
        verbose_name_plural = 'Relacion Items'



