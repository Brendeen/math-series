import pytest
from series import test
from series import fibonacci
from series import lucas
from series import sum_series


def test_exists():
    assert test

# Fibonacci sequence tests


def test_fib_1():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected


def test_fib_2():
    actual = fibonacci(7)
    expected = 13
    assert actual == expected


def test_fib_3():
    actual = fibonacci(15)
    expected = 610
    assert actual == expected


def test_fib_4():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

# Lucas sequence tests


def test_luc_1():
    actual = lucas(1)
    expected = 1
    assert actual == expected


def test_luc_2():
    actual = lucas(2)
    expected = 3
    assert actual == expected


def test_luc_3():
    actual = lucas(3)
    expected = 4
    assert actual == expected


def test_luc_4():
    actual = lucas(10)
    expected = 123
    assert actual == expected


def test_luc_5():
    actual = lucas(15)
    expected = 1364
    assert actual == expected


def test_sum_1():
    actual = sum_series(0)
    expected = 0
    assert actual == expected


def test_sum_2():
    actual = sum_series(1)
    expected = 1
    assert actual == expected


def test_sum_3():
    actual = sum_series(-1)
    expected = 0
    assert actual == expected


def test_sum_4():
    actual = sum_series(4, 5, 6)
    expected = 28
    assert actual == expected


def test_sum_5():
    actual = sum_series(10, 20, 30)
    expected = 2330
    assert actual == expected
