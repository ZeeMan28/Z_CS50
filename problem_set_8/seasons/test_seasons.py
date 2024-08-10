import pytest
from seasons import get_minutes

def test_good():
    test_str = '2024-02-19'
    expected_str = 'five hundred and twenty-five thousand, six hundred minutes'
    assert get_minutes(test_str) == expected_str


def test_bad():
    test_str = '02-30-2023'
    with pytest.raises(ValueError):
        get_minutes(test_str)