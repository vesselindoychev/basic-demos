from django.core.exceptions import ValidationError


def validate_name(value):
    if not value.isalpha():
        raise ValidationError('Value must contain only letters!')


def validate_egn(value):
    if not value.isdigit():
        raise ValidationError('EGN must contain only digits!')


def validate_age(value):
    if value < 0:
        raise ValidationError('Age cannot be negative!')
