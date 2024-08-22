import pytest
from working import convert

def test_minutes():
    with pytest.raises(ValueError):
        convert('cat')
    with pytest.raises(ValueError):
        convert('8:50 AM to 3:70 PM')

def test_hour():
    with pytest.raises(ValueError):
        convert('14:00 PM to 5:00 AM')
    with pytest.raises(ValueError):
        convert('9 AM to 13 PM')
    assert convert('9 AM to 5 PM')== '09:00 to 17:00'
