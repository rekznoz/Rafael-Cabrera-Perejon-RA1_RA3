
from Rafael_Cabrera_Perejon_examenRA1_RA3 import VerificacionEdadMes

def test_VerificacionEdadMes():
    assert VerificacionEdadMes(11,8) == (11,12,13) , "Fallo En la Verificacion de Edad Mes"