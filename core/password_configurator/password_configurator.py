"""Functions to generate passwords"""

import random
import secrets
import string
from typing import NoReturn

from core.password_configurator.exceptions import ConfigurePasswordArgumentsError, Messages

UPPER = string.ascii_uppercase
DIGITS = string.digits
SPECIAL_CHARS = string.punctuation + "àéèùçâêîôû"
LOWER = string.ascii_lowercase


def generate_password(
        length: int = 16,
        nb_digits: int = 4,
        nb_uppers: int = 4,
        nb_special_chars: int = 4
) -> str:
    """
    Generate a password with specified length, number of digits, uppers and special characters
    """
    _check_arguments(length=length, nb_digits=nb_digits, nb_uppers=nb_uppers, nb_special_chars=nb_special_chars)
    nb_lowercase = length - nb_digits - nb_uppers - nb_special_chars
    characters = [secrets.choice(DIGITS) for _ in range(nb_digits)]
    characters.extend([secrets.choice(UPPER) for _ in range(nb_uppers)])
    characters.extend([secrets.choice(SPECIAL_CHARS) for _ in range(nb_special_chars)])
    if nb_lowercase:
        characters.extend([secrets.choice(LOWER) for _ in range(nb_lowercase)])
    random.shuffle(characters)
    return "".join(characters)


def _check_arguments(length:int, nb_digits:int, nb_uppers:int, nb_special_chars:int) -> bool | NoReturn:
    """Validate password_generator function arguments, or raise a GeneratePasswordArgumentsError"""
    if nb_digits > length:
        raise ConfigurePasswordArgumentsError(
            Messages.TOO_MANY_DIGITS.format(length=length, nb_digits=nb_digits))
    if nb_uppers > length:
        raise ConfigurePasswordArgumentsError(
            Messages.TOO_MANY_UPPERS.format(length=length, nb_uppers=nb_uppers))
    if nb_special_chars > length:
        raise ConfigurePasswordArgumentsError(
            Messages.TOO_MANY_SPECIAL_CHARS.format(length=length, nb_special_chars=nb_special_chars))
    if nb_digits + nb_uppers + nb_special_chars > length:
        raise ConfigurePasswordArgumentsError(
            Messages.TOO_MANY_CHARACTERS.format(
                nb_digits=nb_digits, nb_uppers=nb_uppers, nb_special_chars=nb_special_chars, length=length,
        ))
    return True


if __name__ == '__main__':
    print(SPECIAL_CHARS)
    print(generate_password())
