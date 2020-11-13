import pytest
from src.u031_virs_videja import lielaku_skaits

def test_neviens():
    assert lielaku_skaits([1]) == 0

def test_viens_lielaks():
    assert lielaku_skaits([1,3,5]) == 1