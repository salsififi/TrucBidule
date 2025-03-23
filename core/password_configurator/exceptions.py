"""Exceptions for password_generator package"""


class Messages:
    TOO_MANY_DIGITS = ("Le nombre demandé de chiffres ({nb_digits}) est supérieur "
                       "à la longueur totale demandée ({length}).")
    TOO_MANY_UPPERS = ("Le nombre demandé de majuscules ({nb_uppers}) est supérieur "
                       "à la longueur totale demandée ({length}).")
    TOO_MANY_SPECIAL_CHARS = ("Le nombre demandé de caractères spéciaux ({nb_special_chars}) est supérieur "
                              "à la longueur totale demandée ({length}).")
    TOO_MANY_CHARACTERS = ("La somme du nombre demandé de chiffres ({nb_digits}), de majuscules ({nb_uppers}) "
                           "et de caractères spéciaux ({nb_special_chars}) est supérieure "
                           "à la longueur totale demandée({length}).")


class ConfigurePasswordArgumentsError(Exception):
    pass
