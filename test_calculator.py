import calculator
import pytest

def test_add():
    assert 4 == calculator.add(2,2)

def test_substract():
    assert 6 == calculator.subtract(10,4)
