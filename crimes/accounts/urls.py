from django.urls import path

from .views import SignUpView

# Ruta do rejestracji
urlpatterns = [
    path("sign_up/", SignUpView.as_view(), name="sign_up"),
]