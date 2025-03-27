"""Tests for password_configurator module"""

import pytest

from core.password_configurator.exceptions import ConfigurePasswordArgumentsError, Messages
from core.password_configurator.password_configurator import generate_password

LENGTH = 16
NB_DIGITS = 3
NB_UPPERS = 3
NB_SPECIAL_CHARS = 2

@pytest.fixture
def password():
    return generate_password(
        length=LENGTH,
        nb_digits=NB_DIGITS,
        nb_uppers=NB_UPPERS,
        nb_special_chars=NB_SPECIAL_CHARS,
    )

def test_nb_digits(password):
    nb_digits = len([char for char in password if char.isdigit()])
    assert nb_digits == NB_DIGITS

def test_nb_upper(password):
    nb_uppers = len([char for char in password if char.isupper()])
    assert nb_uppers == NB_UPPERS

def test_password_length(password):
    assert len(password) == LENGTH

def test_nb_digits_greater_than_length():
    with pytest.raises(ConfigurePasswordArgumentsError) as exc_info:
        generate_password(length=LENGTH, nb_digits=LENGTH + 1, nb_uppers=NB_UPPERS, nb_special_chars=NB_SPECIAL_CHARS)
    assert str(exc_info.value) == Messages.TOO_MANY_DIGITS.format(
        nb_digits=LENGTH + 1, length=LENGTH
    )

def test_nb_uppers_greater_than_length():
    with pytest.raises(ConfigurePasswordArgumentsError) as exc_info:
        generate_password(length=LENGTH, nb_digits=NB_DIGITS, nb_uppers=LENGTH + 1, nb_special_chars=NB_SPECIAL_CHARS)
    assert str(exc_info.value) == Messages.TOO_MANY_UPPERS.format(
        nb_uppers=LENGTH + 1, length=LENGTH
    )

def test_nb_special_chars_greater_than_length():
    with pytest.raises(ConfigurePasswordArgumentsError) as exc_info:
        generate_password(length=LENGTH, nb_digits=NB_DIGITS, nb_uppers=NB_UPPERS, nb_special_chars=LENGTH + 1)
    assert str(exc_info.value) == Messages.TOO_MANY_SPECIAL_CHARS.format(
        nb_special_chars=LENGTH + 1, length=LENGTH
    )

def test_sum_digits_uppers_and_special_chars_greater_than_length():
    with pytest.raises(ConfigurePasswordArgumentsError) as exc_info:
        generate_password(
            length=LENGTH,
            nb_digits=NB_DIGITS,
            nb_uppers=NB_UPPERS,
            nb_special_chars=LENGTH - NB_DIGITS - NB_UPPERS + 1
        )
    assert str(exc_info.value) == Messages.TOO_MANY_CHARACTERS.format(
        length=LENGTH,
        nb_digits=NB_DIGITS,
        nb_uppers=NB_UPPERS,
        nb_special_chars=LENGTH - NB_DIGITS - NB_UPPERS + 1,
    )
