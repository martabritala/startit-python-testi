import pytest
from src.u021_summa import summa

def test_1_un_1():
    assert summa(1, 1) == 2


def test_poz_neg():
    assert summa(-5,10)==5