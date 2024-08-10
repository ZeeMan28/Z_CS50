from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("12/34") == 35

    with pytest.raises(ValueError):
        convert("five/six")

    with pytest.raises(ZeroDivisionError):
        convert("5/0")


def test_gauge():
    assert gauge(35) == "35%"
    assert gauge(99) == "F"
    assert gauge(1) == "E"

