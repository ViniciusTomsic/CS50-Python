from jar import Jar
import pytest

def test_init():
    with pytest.raises(ValueError):
        jar= Jar('cat')

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert jar.size== 1
    jar.deposit(3)
    assert jar.size== 4
    with pytest.raises(ValueError):
        jar.deposit(10)


def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(1)
    assert jar.size== 9
    with pytest.raises(ValueError):
        jar.withdraw(10)

