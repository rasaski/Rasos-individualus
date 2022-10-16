from django.urls import path
from .views import index, sign_up, foods, contacts

urlpatterns = [
    path('', index, name='index'),
    path('registration/sign_up', sign_up, name='sign_up'),
    path('foods', foods, name='foods'),
    path('contacts', contacts, name='contacts'),
]
