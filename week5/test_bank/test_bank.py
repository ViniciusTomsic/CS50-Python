from bank import value

def test_hello():
    assert value('hello, tom')==0
    assert value('HELLO')==0

def test_20():
    assert value('Hey, men')== 20
    assert value('How you doin?')== 20

def test_100():
    assert value('Whats up?')==100
    assert value('Good morning')==100

