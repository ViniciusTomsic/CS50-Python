import plates

def test_pontuation():
    assert plates.is_valid("What's up?")==False
    assert plates.is_valid("Hello, mam")==False
    assert plates.is_valid("<>[")==False
    assert plates.is_valid('PT.12')== False

def test_zeros():
    assert plates.is_valid('CS005')== False
    assert plates.is_valid('CS50')== True

def test_midle():
    assert plates.is_valid('50CS')== False
    assert plates.is_valid('CS50')== True
    assert plates.is_valid('AAA22A')== False
def test_is_valid():
    assert plates.is_valid('CSABC140')== False
    assert plates.is_valid('50')== False
    assert plates.is_valid('A')== False


