from django.core.validators import MinLengthValidator
from django.db import models


class Department(models.Model):
    SYSTEM_SOFTWARE = 'System Software'
    PRODUCT_MARKETING = 'Product Marketing'
    SECURITY = 'Security'
    MOBILE_APP = 'Mobile App'

    DEPARTMENTS = (
        SYSTEM_SOFTWARE,
        PRODUCT_MARKETING,
        SECURITY,
        MOBILE_APP,
    )

    name = models.CharField(
        max_length=max(len(d) for d in DEPARTMENTS),
        choices=((d, d) for d in DEPARTMENTS),
    )

    def __str__(self):
        return f'{self.name}'


class Employee(models.Model):
    FIRST_NAME_MAX_LENGTH = 30
    FIRST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2

    SOFTWARE_DEVELOPER = 'Software Developer'
    QA_ENGINEER = 'QA Engineer'
    DEVOPS_SPECIALIST = 'DevOps Specialist'

    JOB_TITLES = (
        SOFTWARE_DEVELOPER,
        QA_ENGINEER,
        DEVOPS_SPECIALIST,
    )

    SOFT_UNI = 'SoftUni'
    GOOGLE = 'Google'
    FACEBOOK = 'Facebook'
    INSTAGRAM = 'Instagram'

    COMPANIES = (
        SOFT_UNI,
        GOOGLE,
        FACEBOOK,
        INSTAGRAM,
    )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
        )
    )

    egn = models.CharField(
        max_length=10,
        unique=True,
        null=True,
        blank=True,
        verbose_name='EGN',
        validators=(
            MinLengthValidator(10),
        )
    )

    job_title = models.CharField(
        max_length=max(len(j) for j in JOB_TITLES),
        choices=((j, j) for j in JOB_TITLES),
    )

    company = models.CharField(
        max_length=max(len(c) for c in COMPANIES),
        choices=((c, c) for c in COMPANIES),
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
    )
