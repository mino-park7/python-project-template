"""Test for my_project."""

from my_project import Calculator


def test_calculator_add():
    """Test the add method of the Calculator class."""
    calc = Calculator()
    assert calc.add(2.0, 3.0) == 5.0


def test_calculator_subtract():
    """Test the subtract method of the Calculator class."""
    calc = Calculator()
    assert calc.subtract(5.0, 3.0) == 2.0
