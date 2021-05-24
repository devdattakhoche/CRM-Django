from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from leads import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("leads/", include("leads.urls", namespace="leads")),
    path("landing/", views.LandingView.as_view(), name="landing_page"),
]

if settings.DEBUG:

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
