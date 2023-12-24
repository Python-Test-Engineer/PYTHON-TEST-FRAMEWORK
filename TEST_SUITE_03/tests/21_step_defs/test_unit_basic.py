# type: ignore

"""
This module contains step definitions for unit_basic.feature.
Decorators for step definition functions are simplified using partials.
"""

from functools import partial

from pytest_bdd import given, parsers, scenarios, then, when

from src.cucucmber.cucumbers import CucumberBasket

# Partial Step Helpers

CONVERTERS = {
    "initial": int,
    "some": int,
    "total": int,
}

given_basket = partial(given, target_fixture="basket", converters=CONVERTERS)  # type: ignore
when_cukes = partial(when, converters=CONVERTERS)  # type: ignore
then_cukes = partial(then, converters=CONVERTERS)  # type: ignore


# Scenarios

scenarios("../features/unit_basic.feature")


# Given Steps


@given_basket(parsers.re(r'the basket has "(?P<initial>\d+)" cucumber(s?)'))  # type: ignore
def basket_init(initial):
    """Doc"""
    return CucumberBasket(initial_count=initial)


@given_basket("the basket is empty")
def basket_empty():
    """Doc"""
    return CucumberBasket()


@given_basket("the basket is full")
def basket_full():
    """Doc"""
    return CucumberBasket(initial_count=10)


# When Steps


@when_cukes(parsers.re(r'"(?P<some>\d+)"( more)? cucumber(s?) are added to the basket'))
def add_cucumbers(basket, some):
    """Doc"""
    basket.add(some)


@when_cukes(
    parsers.re(r'"(?P<some>\d+)"( more)? cucumber(s?) are removed from the basket')
)
def remove_cucumbers(basket, some):
    """Doc"""
    basket.remove(some)


# Then Steps


@then_cukes(parsers.re(r'the basket contains "(?P<total>\d+)" cucumbers'))
def basket_has_total(basket, total):
    """Doc"""
    assert basket.count == total


@then_cukes("the basket is empty")
def basket_is_empty(basket):
    """Doc"""
    assert basket.empty


@then_cukes("the basket is full")
def basket_is_full(basket):
    """Doc"""
    assert basket.full


@then_cukes(parsers.re(r'"(?P<some>\d+)" cucumbers cannot be added to the basket'))
def cannot_add_more(basket, some):
    """Doc"""
    count = basket.count
    try:
        basket.add(some)
    except ValueError as e:
        assert str(e) == "Attempted to add too many cucumbers"
        assert count == basket.count, "Cucumber count changed despite overflow"
    else:
        assert False, "ValueError was not raised for basket overflow"


@then_cukes(parsers.re(r'"(?P<some>\d+)" cucumbers cannot be removed from the basket'))
def cannot_remove_more(basket, some):
    """Doc"""
    count = basket.count
    try:
        basket.remove(some)
    except ValueError as e:
        assert str(e) == "Attempted to remove too many cucumbers"
        assert count == basket.count, "Cucumber count changed despite overdraw"
    else:
        assert False, "ValueError was not raised for basket overdraw"
