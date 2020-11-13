import pytest
from src.u023_hipotenuza import hipotenuza

def test_3_un_4():
    assert hipotenuza(3,4)==5


def test_dalas():
    assert hipotenuza(3,7)== pytest.approx(7.616, rel=0.001) 