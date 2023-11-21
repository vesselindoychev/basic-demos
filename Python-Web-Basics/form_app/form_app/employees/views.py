from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.shortcuts import render, redirect

from form_app.employees.models import Employee


def validate_age(value):
    if value < 0:
        raise ValidationError('Value must be positive!')

    if value > 100:
        raise ValidationError('Value must be 100 or below')

    if value < 18:
        raise ValidationError('Value must be 18 or above')


def validate_egn(value):
    for ch in value:
        if ch.isalpha():
            raise ValidationError('Value must contain only digits!')


"""
Normal Forms
"""

# class EmployeeForm(forms.Form):
#     first_name = forms.CharField(
#         max_length=30,
#
#         widget=forms.TextInput(
#             attrs={'placeholder': 'Enter First name',
#                    'class': 'form-control',
#                    }
#         )
#
#     )
#
#     last_name = forms.CharField(
#         max_length=30,
#         widget=forms.TextInput(
#             attrs={'placeholder': 'Enter Last name',
#                    'class': 'form-control'}
#         )
#     )
#
#     egn = forms.CharField(
#         max_length=10,
#         validators=(
#             MinLengthValidator(10),
#             validate_egn,
#         ),
#     )
#
#     job_title = forms.ChoiceField(
#         choices=(
#             (1, 'Software Developer'),
#             (2, 'QA Engineer'),
#             (3, 'DevOps Specialist'),
#         ),
#
#     )
#
#     company = forms.ChoiceField(
#         choices=((c, c) for c in Employee.COMPANIES)
#     )
# age = forms.IntegerField(
#     widget=forms.NumberInput(
#         attrs={
#             'placeholder': 'Age',
#         }
#     ),
#     validators=(
#         validate_age,
#     ),
#
# )
#
# comment = forms.CharField(
#     widget=forms.Textarea(),
#     required=False,
# )
#
# BIRTH_YEAR_CHOICES = [i for i in range(2000, 2022 + 1, 1)]
#
# birth_year = forms.DateField(
#     widget=forms.SelectDateWidget(
#         years=BIRTH_YEAR_CHOICES
#     ),
#     required=False,
# )
#
# BLUE = 'Blue'
# GREEN = 'Green'
# BLACK = 'Black'
#
# FAVORITE_COLORS_CHOICES = (
#     BLUE,
#     GREEN,
#     BLACK,
# )
#
# favorite_colors = forms.MultipleChoiceField(
#     required=False,
#     widget=forms.CheckboxSelectMultiple(),
#     choices=((c, c) for c in FAVORITE_COLORS_CHOICES),
# )
# email = forms.EmailField(
#     widget=(
#         forms.EmailInput(
#             attrs={
#                 'placeholder': 'Email',
#             }
#         )
#     ),
#     required=False,
# )
#
# password = forms.CharField(
#     max_length=20,
#     required=False,
#     validators=(
#         MinLengthValidator(5),
#     ),
#     widget=(
#         forms.PasswordInput(
#             attrs={
#                 'placeholder': 'Password',
#             }
#         )
#     ),
#
# )
#
# url = forms.URLField(
#     widget=(
#         forms.URLInput(
#             attrs={
#                 'placeholder': 'URL Field',
#             }
#         )
#     ),
#     required=False,
# )
#
# AUDI = 'Audi'
# BMW = 'BMW'
# MERCEDES = 'Mercedes'
#
# CARS = (AUDI,
#         BMW,
#         MERCEDES,
#         )
#
# cars = forms.ChoiceField(
#     choices=((c, c) for c in CARS),
#     required=False,
# )


"""
Model Forms
"""


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        # fields = ('first_name', 'last_name')

        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Fill First name'}
            ),
            'last_name': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Fill Last name'}
            ),

        }


class EditEmployeeForm(EmployeeForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'egn': forms.TextInput(
                attrs={'readonly': 'readonly'},
            )
        }


class EmployeeOrderForm(forms.Form):
    order_by = forms.ChoiceField(
        choices=(
            ('first_name', 'First Name'),
            ('last_name', 'Last Name'),
            ('company', 'Company'),
        ),

    )


def show_home(request):
    return render(request, 'index.html')


def create_employee(request):
    if request.method == 'POST':
        employee_form = EmployeeForm(request.POST)

        if employee_form.is_valid():
            # 1st way
            #
            # emp = Employee(
            #     first_name=employee_form.cleaned_data['first_name'],
            #     last_name=employee_form.cleaned_data['last_name'],
            #     job_title=employee_form.cleaned_data['job_title'],
            #     company=employee_form.cleaned_data['company'],
            #     department=employee_form.cleaned_data['department'],
            # )

            # ------------------------------------------------------------

            # 2nd way
            # emp = Employee(
            #     **employee_form.cleaned_data,
            #     department_id=1,
            # )
            #
            # emp.save()
            employee_form.save()
            return redirect('index')
    else:
        employee_form = EmployeeForm()

    employee_order_form = EmployeeOrderForm(request.GET)
    employee_order_form.is_valid()

    order_by = employee_order_form.cleaned_data.get('order_by', 'first_name')

    context = {
        'employee_form': employee_form,
        'employees': Employee.objects.order_by(order_by).all(),
        'employee_order_form': employee_order_form,
    }

    return render(request, 'create.html', context)


def edit_employee(request, pk):
    employee = Employee.objects.get(pk=pk)

    if request.method == 'POST':
        # if you want the EditForm to work, change the employee_form with EditEmployeeForm
        employee_form = EmployeeForm(request.POST, instance=employee)

        if employee_form.is_valid():
            employee_form.save()
            return redirect('create employee')

    else:
        employee_form = EmployeeForm(instance=employee)

    context = {
        'employee': employee,
        'employee_form': employee_form,
    }

    return render(request, 'edit.html', context)
