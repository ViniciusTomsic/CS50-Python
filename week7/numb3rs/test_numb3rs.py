from numb3rs import validate

def test_missingnumbers():
    assert validate('234.43')== False
    assert validate('cat')== False

def test_outofrange():
    assert validate('265.2.2.2')== False
    assert validate('2.1000.10000.2')== False
    assert validate('1.1.1.290')== False
    assert validate('1.1.1.1.1')== False
