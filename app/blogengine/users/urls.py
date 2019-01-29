from django.urls import path
from .views import UserRegistrationView

app_name = 'users'

urlpatterns =[
    path('accounts/register/',UserRegistrationView.as_view(),name='register'),

]
