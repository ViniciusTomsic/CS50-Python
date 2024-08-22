from seasons import converter
import pytest

def test_main():
    assert converter('1999-01-01','2000-01-01')== 'Five hundred twenty-five thousand, six hundred minutes'
    assert converter('2001-01-01','2003-01-01')== "One million, fifty-one thousand, two hundred minutes"
    assert converter('1995-01-01','2000-01-01')== "Two million, six hundred twenty-nine thousand, four hundred forty minutes"
    assert converter('2020-06-01','2032-01-01')== "Six million, ninety-two thousand, six hundred forty minutes"
    assert converter('1998-06-20','2000-01-01')== "Eight hundred six thousand, four hundred minutes"

def test_invalid():
    with pytest.raises(SystemExit):
        converter('cat')

