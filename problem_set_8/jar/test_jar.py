from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12

    jar1 = Jar(5)
    assert jar1.capacity == 5


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(10)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(9)

    assert jar.size == 9


def test_withdraw():
    jar = Jar()
    jar.deposit(11)
    jar.withdraw(9)

    assert jar.size == 2