from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static

# Ruty pliku głównego, tutaj definiujemy tylko nowe aplikacje
urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path('', include('accounts.urls')),
    path('', include('app_crimes_comparison.urls')),
    path("", TemplateView.as_view(template_name="index.html"), name="index"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
