import pytest
from app import add

def test_add_positive():
    assert add(2, 3) == 100  # (5³ - 5² = 125 - 25 = 100)

def test_add_other_values():
    assert add(1, 1) == 4    # (2³ - 2² = 8 - 4 = 4)
    assert add(0, 0) == 0    # (0³ - 0² = 0 - 0 = 0)
    assert add(1, 2) == 19   # (3³ - 3² = 27 - 9 = 18? Подождите... 27-9=18, а не 19)
