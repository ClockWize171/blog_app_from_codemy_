from django.urls import path,include
from .views import (
    UserRegisterView as urv
)
urlpatterns = [
    path('register/', urv.as_view(), name='register')
]