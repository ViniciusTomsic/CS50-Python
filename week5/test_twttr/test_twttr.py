from twttr import shorten

def test_shorten():
    assert shorten('David')=='Dvd'
    assert shorten("HELLO")== 'HLL'
    assert shorten('CS50')== 'CS50'
    assert shorten("What's up?")== "Wht's p?"

