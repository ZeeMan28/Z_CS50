from bank import value

def test_bank():
    assert value("hello") == 0
    assert value("hi") == 20
    assert value("bonjour") == 100
    assert value("HELLO") == 0
