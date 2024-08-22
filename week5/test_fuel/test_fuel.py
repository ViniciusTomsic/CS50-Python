from fuel import convert, gauge
import pytest

def test_convert():
    with pytest.raises(ValueError):
        convert('cat/dog')
    assert convert('1/4')== 25
    with pytest.raises(ZeroDivisionError):
        convert('1/0')


def test_gauge():
    assert gauge(50)== '50%'
    assert gauge(0)== 'E'
    assert gauge(1)== 'E'
    assert gauge(99)== 'F'
