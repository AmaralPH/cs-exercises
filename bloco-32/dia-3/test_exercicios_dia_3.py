import pytest
from codigo import create_fizz_buzz_list, translate_letter_to_numbers


def test_lista_fizz_buzz_returns_fizz_instead_multiple_of_3():
    assert create_fizz_buzz_list(3)[2] == "Fizz"


def test_lista_fizz_buzz_returns_buzz_instead_multiple_of_5():
    assert create_fizz_buzz_list(5)[4] == "Buzz"


def test_lista_fizz_buzz_returns_fizzbuzz_instead_multiple_of_5_and_3():
    assert create_fizz_buzz_list(15)[14] == "FizzBuzz"


def test_number_letters_association_to_ADGJMPT01():
    assert translate_letter_to_numbers('ADGJMPTW-01') == "23456789-01"


def test_number_letters_association_when_input_have_more_than_30_chars():
    with pytest.raises(ValueError):
        translate_letter_to_numbers('ABCDEFGHIJKLMNOPQRSTUVXYZABCDEFG')


def test_number_letters_association_when_input_is_empty():
    with pytest.raises(ValueError):
        translate_letter_to_numbers('')


def test_number_letters_association_when_input_is_invalid():
    with pytest.raises(ValueError):
        translate_letter_to_numbers('abc736')
