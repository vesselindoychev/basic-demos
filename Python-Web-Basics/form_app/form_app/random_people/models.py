from django.core.validators import MinLengthValidator
from django.db import models

from form_app.random_people.validators import validate_name, validate_egn, validate_age


class Pet(models.Model):
    PET_NAME_MAX_LENGTH = 15
    PET_NAME_MIN_LENGTH = 2

    DOG = 'Dog'
    CAT = 'Cat'
    FISH = 'Fish'
    PARROT = 'Parrot'
    BUNNY = 'Bunny'
    PIG = 'Pig'

    PET_TYPES = (
        DOG,
        CAT,
        FISH,
        PARROT,
        BUNNY,
        PIG,
    )

    pet_type = models.CharField(
        max_length=max(len(t) for t in PET_TYPES),
        choices=((t, t) for t in PET_TYPES)
    )

    pet_name = models.CharField(
        max_length=PET_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(PET_NAME_MIN_LENGTH),
            validate_name,
        )
    )

    age = models.IntegerField(
        validators=(
            validate_age,
        )
    )

    image = models.ImageField(
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.pet_name} ({self.pet_type}) - {self.age} years old'


class Person(models.Model):
    FIRST_NAME_MAX_LENGTH = 15
    FIRST_NAME_MIN_LENGTH = 5
    LAST_NAME_MAX_LENGTH = 15
    LAST_NAME_MIN_LENGTH = 5
    EGN_MAX_LENGTH = 10
    EGN_MIN_LENGTH = 10

    WAITER = 'Waiter'
    INTERPRETER = 'Interpreter'
    DRIVER = 'Driver'
    SOFTWARE_ENGINEER = 'Software Engineer'
    TEACHER = 'Teacher'
    PLUMBER = 'Plumber'

    JOB_TITLES = (
        WAITER,
        INTERPRETER,
        DRIVER,
        SOFTWARE_ENGINEER,
        TEACHER,
        PLUMBER,
    )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            validate_name,
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            validate_name,
        )
    )

    egn = models.CharField(
        max_length=EGN_MAX_LENGTH,
        validators=(
            MinLengthValidator(EGN_MIN_LENGTH),
            validate_egn,
        ),
        unique=True,
    )

    job_title = models.CharField(
        max_length=max(len(j) for j in JOB_TITLES),
        choices=((j, j) for j in JOB_TITLES),
    )

    image = models.ImageField(
        null=True,
        blank=True,
    )

    pet_type = models.ForeignKey(
        Pet,
        on_delete=models.CASCADE,
    )
