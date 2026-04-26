
import pytest
from app import add

def test_add_positive():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, -1) == -2

def test_add_float():
    assert add(2.5, 2.5) == 5.0

def test_add_invalid():
    with pytest.raises(ValueError):
        add("2", 3)
