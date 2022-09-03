from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def state_product_should_be_greater_than_four(value):
    common_size_for_strings(value)


def category_size_should_be_greater_than_four(value):
    common_size_for_strings(value)


def common_size_for_strings(value):
    if len(value) < 5:
        raise ValidationError(
            _('%(value)s should be greater than 4 letters'),
            params={'value': value},
        )


def should_not_have_special_characters(value):
    matches = ["+", "*", "/", "-", "_", "ç", "!", "¡", "¨", ":", "@", ";", "}", "{", "]", "[", "^", "¿", "?", "=", "%",
               "(", ")", "<", ">", "Ç",
               "$", "&"]
    if any(x in value for x in matches):
        raise ValidationError(
            _('%(value)s must not have special characters'),
            params={'value': value},
        )


def should_not_have_spaces(value):
    if str(value).__contains__(" "):
        raise ValidationError(
            _('Spaces are not valid in this field'),
            params={'value': value},
        )


def should_be_alphabetic(value):
    if not str(value).isalpha():
        raise ValidationError(
            _('%(value)s should be alphabetic'),
            params={'value': value},
        )


def characters_size_should_be_grater_than_two(value):
    if len(value) < 3:
        raise ValidationError(
            _('%(value)s should be greater than 2 letters'),
            params={'value': value},
        )


def cellphone_number_size_is_ten(value):
    if len(value) != 10:
        raise ValidationError(
            _('%(value)s should be equals to 10 digits'),
            params={'value': value},
        )


def identification_number_size_should_be_greater_than_seven(value):
    if len(value) < 7:
        raise ValidationError(
            _('%(value)s should be greater than 7 digits'),
            params={'value': value},
        )


def is_number(value):
    if not str(value).isnumeric():
        raise ValidationError(
            _('%(value)s should be a number'),
            params={'value': value},
        )