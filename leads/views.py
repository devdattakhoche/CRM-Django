from django.shortcuts import redirect, render
from .models import Lead
from .forms import LeadModelForm, Leadform
from django.views import generic
from django.urls import reverse
from django.core.mail import send_mail


class LandingView(generic.TemplateView):
    template_name = "landing.html"


def landing_page(request):
    return render(request, "landing.html")


class LeadListView(generic.ListView):
    template_name = "leads/lead_list.html"
    context_object_name = "leads"  # default object name 'object_list'
    model = Lead  # pass model or queryset
    # queryset = Lead.objects.all()


def lead_list(request):
    leads = Lead.objects.all()
    params = {"leads": leads}
    return render(request, "leads/lead_list.html", params)


class LeadDetailView(generic.DetailView):
    # default pk is needed in url
    template_name = "leads/lead_detail.html"
    context_object_name = "lead"
    model = Lead  # pass model or queryset
    # queryset = Lead.objects.all()


def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    params = {"lead": lead}
    return render(request, "leads/lead_detail.html", params)


class LeadCreateView(generic.CreateView):
    model = Lead
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm

    def form_valid(self, form):
        send_mail(
            subject="A lead has been created",
            message="Go to the site to see the new lead",
            from_email="test@test.com",
            recipient_list=["test2@test.com"],
        )
        return super(LeadCreateView, self).form_valid(form)

    def get_success_url(self) -> str:
        return reverse("leads:lead_list")


def lead_create(request):
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("leads:lead_list")
    params = {"form": LeadModelForm()}
    return render(request, "leads/lead_create.html", params)


class LeadUpdateView(generic.UpdateView):
    model = Lead
    form_class = LeadModelForm
    template_name = "leads/lead_update.html"

    def get_success_url(self) -> str:
        return reverse("leads:lead_list")


def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)

    if request.method == "POST":
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            lead.save()
            return redirect("lead_list")
    params = {"form": LeadModelForm(instance=lead), "lead": lead}
    return render(request, "leads/lead_update.html", params)


class LeadDeleteView(generic.DeleteView):
    model = Lead
    # Delete view by default gives us a form to submit , so we can mention it in template
    def get_success_url(self) -> str:
        return reverse("leads:lead_list")


def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect("leads:lead_list")


## FORMS

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
