from myproject import Calculator


def test_calculator_add():
    calc = Calculator()
    assert calc.add(2.0, 3.0) == 5.0


def test_calculator_subtract():
    calc = Calculator()
    assert calc.subtract(5.0, 3.0) == 2.0
