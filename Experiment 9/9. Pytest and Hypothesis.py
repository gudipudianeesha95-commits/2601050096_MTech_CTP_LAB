from calculator import add, multiply, calculate_total

from hypothesis import given, strategies as st


def test_add():
    assert add(10, 20) == 30


def test_multiply():
    assert multiply(5, 4) == 20


def test_calculate_total():
    price = 100
    quantity = 5

    total = calculate_total(price, quantity)

    assert total == 500


@given(st.integers(), st.integers())
def test_add_property(a, b):
    assert add(a, b) == a + b