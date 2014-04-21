from django.test import TestCase



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







