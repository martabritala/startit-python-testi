import pytest
from src.u022_linears_vienadojums import vienadojums

def test_1_1_1():
    assert vienadojums (1, 1, 1.1) == 2.1