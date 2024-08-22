from um import count

def test_1():
    assert count('um...')== 1
    assert count('Um, i dont know')==1

def test_0():
    assert count('hello yummt')==0
    assert count('hi there Kuminga')==0

def test_plus():
    assert count('um, let me see, um, maybe')== 2
    assert count('um... um, um, um')== 4
