from django.contrib import admin
from django.urls import path
from .views import dane, sign_up, index
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from . import views

# Ruty do poszczególnych podstron oraz funkcji np.login/logout
urlpatterns = [
    path("admin/", admin.site.urls),
    path('dane/', dane, name='dane'),
    path('sign_up/', sign_up, name='sign_up'),
    path('index', index, name='index'),
    path('login/', auth_views.LoginView.as_view()),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('generate_wykres/', views.generate_wykres, name='generate_wykres')
]
