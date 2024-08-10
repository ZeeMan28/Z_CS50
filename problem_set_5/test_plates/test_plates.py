from plates import is_valid

def test_iv_letters():
    assert is_valid("CS50") == True
    assert is_valid("50") == False


def test_iv_numbers():
    assert is_valid("CS50") == True
    assert is_valid("C50S") == False
    assert is_valid("CS05") == False


def test_iv_characters():
    assert is_valid("GOODBYE") == False
    assert is_valid("GOODBY") == True

def test_iv_extra():
    assert is_valid("GOODBY") == True
    assert is_valid("GOODB.") == False
    assert is_valid("GO DBY") == False


# “All vanity plates must start with at least two letters.”

# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”

# “Numbers cannot be used in the middle of a plate; they must come at the end.

# “No periods, spaces, or punctuation marks are allowed.”
