from django.urls import path
from . import views


app_name = "leads"

urlpatterns = [
    path("", views.lead_list, name="lead_list"),
    path("<int:id>/", views.lead_detail, name="lead_detail"),
    path("create/", views.lead_create, name="lead_create"),
    path("<int:id>/update/", views.lead_update, name="lead_update"),
    path("<int:id>/delete/", views.lead_delete, name="lead_delete"),
]
