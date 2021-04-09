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

def test_list():
    list=[1,2,3,4,5]
    assert 6 == calculator.Append_list(list)

def test_reverse_string():
    s='ketan'
    rev=calculator.reverse_string(s)
    if rev == 'natek':
        assert True
    else:
        assert False

def test_status_code():
    response=calculator.url_status_code()
    assert 200 == response

def test_uppercase_string():
    s=calculator.string_uppercase('ketan')
    assert 'KETAN' == s

@pytest.mark.repeat(3)
def test_remove_duplicate():
    expected_string='Ketan'
    actual_string=calculator.remove_duplicate('Keetan')
    assert actual_string == expected_string