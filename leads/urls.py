from django.urls import path
from . import views


app_name = "leads"

urlpatterns = [
    path("", views.LeadListView.as_view(), name="lead_list"),
    path("<int:pk>/", views.LeadDetailView.as_view(), name="lead_detail"),
    path("create/", views.LeadCreateView.as_view(), name="lead_create"),
    path("<int:pk>/update/", views.LeadUpdateView.as_view(), name="lead_update"),
    path("<int:pk>/delete/", views.lead_delete, name="lead_delete"),
]
