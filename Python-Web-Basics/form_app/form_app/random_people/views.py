from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django import forms

from form_app.random_people.models import Person, Pet


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First name',
                    'class': 'form-control'}
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Last name',

                },
            ),
        }


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'

        widgets = {
            'pet_name': forms.TextInput(
                attrs={
                    'placeholder': 'Pet name',
                },
            ),
            'age': forms.NumberInput(
                attrs={
                    'placeholder': 'Age',
                },
            ),
        }


def show_home(request):
    return render(request, 'people_index.html')


def create_pet(request):
    if request.method == 'POST':
        pet_form = PetForm(request.POST, request.FILES)
        if pet_form.is_valid():
            pet_form.save()
            return redirect('create person')

    else:
        pet_form = PetForm()

    pets = Pet.objects.prefetch_related('person_set').all()
    context = {
        'pet_form': pet_form,
        'pets': pets,
    }

    return render(request, 'create_pet.html', context)


def edit_pet(request, pk):
    pet = Pet.objects.get(pk=pk)

    if request.method == 'POST':
        pet_form = PetForm(request.POST, request.FILES, instance=pet)
        if pet_form.is_valid():
            pet_form.save()
            return redirect('create person')

    else:
        pet_form = PetForm(instance=pet)

    context = {
        'pet': pet,
        'pet_form': pet_form,
    }

    return render(request, 'edit_pet.html', context)


def create_person(request):
    if request.method == 'POST':
        person_form = PersonForm(request.POST, request.FILES)

        if person_form.is_valid():
            person_form.save()
            return redirect('create person')

    else:
        person_form = PersonForm()

    people = Person.objects.all()
    context = {
        'person_form': person_form,
        'people': people,
    }

    return render(request, 'random_create.html', context)


def edit_person(request, pk):
    person = Person.objects.get(pk=pk)

    if request.method == 'POST':
        person_form = PersonForm(request.POST, request.FILES, instance=person)
        if person_form.is_valid():
            person_form.save()
            return redirect('create person')
    else:
        person_form = PersonForm(instance=person)

    context = {
        'person': person,
        'person_form': person_form,
    }

    return render(request, 'edit_person.html', context)
