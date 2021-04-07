import calculator
import pytest

def test_add():
    assert 4 == calculator.add(2,2)

def test_substract():
    assert 6 == calculator.subtract(10,4)

def test_multiplication():
    assert 9 == calculator.multiply(3,3)

def test_divide():
    assert 2 == calculator.devide(10,5)
