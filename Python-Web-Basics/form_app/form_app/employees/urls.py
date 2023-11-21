from django.urls import path

from form_app.employees.views import show_home, create_employee, edit_employee

urlpatterns = (
    path('', show_home, name='index'),
    path('create/', create_employee, name='create employee'),
    path('edit/<int:pk>/', edit_employee, name='edit employee'),
)
