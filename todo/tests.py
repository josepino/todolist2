from django.test import TestCase
from todo.models import *
#from todo.models import Proyecto
#from todo.models import Fase


#### Pruebas unitarias ####
class TimeDelta:
    """
    Clase TimeDelta
    Recibimos segundos y retornamos el valor en segundos tambien para verificar si funciona correctamente
    """
    def __init__(self, _seconds):
        self.seconds = _seconds

    @property
    def minutes (self):
        return self.seconds / 60.0



### Prueba de tiempo ###
class TimeDeltaTest(TestCase):
    """
    Clase TimeDeltaTest
    Utilizado para probar TimeDelta, le pasamos los parametros y esperamos un retorno correcto
    """
    def test_seconds_deberia_retornar_86400_cuando_se_pasan_86400_al_constructor(self):
        delta = TimeDelta(86400)
        self.assertEqual(delta.seconds, 86400)


""" Pruebas de modelos """
class ModelosTest(TestCase):
    """ Prueba de Proyecto """
    def test_proyecto(self):
        p = Proyecto ()
        p.Nombre = "ProyectoNameTest1"
        p.FechaCreacion = "15/05/2014"
        self.assertEqual("ProyectoNameTest1", p.Nombre)
        self.assertEqual("15/05/2014", p.FechaCreacion)

    """ Prueba de Fase """
    def test_fase(self):
        f = Fase ()
        f.Nombre = "FaseNameTest1"
        self.assertEqual("FaseNameTest1", f.Nombre)

    """ Prueba de TipoItem """
    def test_tipoItem(self):
        ti = TipoItem ()
        ti.Nombre = "TipoItemNameTest1"
        self.assertEqual("TipoItemNameTest1", ti.Nombre)

    """ Prueba de AtributoTipoItem """
    def test_atributoTipoItem(self):
        ati = AtributoTipoItem ()
        ati.Nombre = "AtributoTipoItemNameTest1"
        self.assertEqual("AtributoTipoItemNameTest1", ati.Nombre)

    """ Prueba de Item """
    def test_Item(self):
        it = Item ()
        it.Nombre = "ItemNameTest1"
        self.assertEqual("ItemNameTest1", it.Nombre)

    """ Prueba de AtributoItem """
    def test_atributoItem(self):
        ai = AtributoItem ()
        ai.Nombre = "AtributoItemNameTest1"
        self.assertEqual("AtributoItemNameTest1", ai.Nombre)

    """ Prueba de RelacionItem """
    def test_relacionItem(self):
        ri = RelacionItem ()
        ri.Nombre = "AtributoItemNameTest1"
        self.assertEqual("AtributoItemNameTest1", ri.Nombre)                









