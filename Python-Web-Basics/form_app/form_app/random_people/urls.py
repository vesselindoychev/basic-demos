from django.urls import path

from form_app.random_people.views import show_home, create_person, create_pet, edit_person, edit_pet

urlpatterns = (
    path('', show_home, name='people home'),
    path('create/', create_person, name='create person'),
    path('create/pet/', create_pet, name='create pet'),
    path('edit/person/<int:pk>/', edit_person, name='edit person'),
    path('edit/pet/<int:pk>/', edit_pet, name='edit pet'),
)
