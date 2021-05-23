from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Agent, Lead
from .forms import LeadModelForm, Leadform


def lead_list(request):
    leads = Lead.objects.all()
    params = {"leads": leads}
    return render(request, "leads/lead_list.html", params)


def lead_detail(request, id):
    lead = Lead.objects.get(id=id)
    params = {"lead": lead}
    return render(request, "leads/lead_detail.html", params)


def lead_create(request):
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lead_list")
    params = {"form": LeadModelForm()}
    return render(request, "leads/lead_create.html", params)


def lead_update(request, id):
    lead = Lead.objects.get(id=id)

    if request.method == "POST":
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            lead.save()
            return redirect("lead_list")
    params = {"form": LeadModelForm(instance=lead), "lead": lead}
    return render(request, "leads/lead_update.html", params)


def lead_delete(request, id):
    lead = Lead.objects.get(id=id)
    lead.delete()
    return redirect("lead_list")


# def lead_update(request, id):
#     lead = Lead.objects.get(id=id)

#     if request.method == "POST":
#         form = Leadform(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             lead.first_name = form.cleaned_data["first_name"]
#             lead.last_name = form.cleaned_data["last_name"]
#             lead.age = form.cleaned_data["age"]
#             lead.save()
#             return redirect("lead_list")
#     params = {"form": Leadform(lead.__dict__), "lead": lead}
#     return render(request, "leads/lead_update.html", params)


# def lead_create(request):
#     if request.method == "POST":
#         form = Leadform(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             agent = Agent.objects.first()
#             first_name = form.cleaned_data["first_name"]
#             last_name = form.cleaned_data["last_name"]
#             age = form.cleaned_data["age"]
#             Lead.objects.create(
#                 first_name=first_name, last_name=last_name, age=age, agent=agent
#             )
#             return redirect("lead_list")
#     params = {"form": Leadform()}
#     return render(request, "leads/lead_create.html", params)
