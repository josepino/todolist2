from django.test import TestCase



#### Pruebas unitarias ####
class TimeDelta:
    def __init__(self, _seconds):
        self.seconds = _seconds

    @property
    def minutes (self):
        return self.seconds / 60.0



### Prueba de tiempo ###
class TimeDeltaTest(TestCase):
    def test_seconds_deberia_retornar_86400_cuando_se_pasan_86400_al_constructor(self):
        delta = TimeDelta(86400)
        self.assertEqual(delta.seconds, 86400)







