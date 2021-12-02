# from django.http import HttpResponse
# from django.shortcuts import render
from authentication.models import Worker
from django.views.generic import TemplateView

# def first_view(request):
#     return HttpResponse("first view")


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        workers = Worker.objects.all().first()
        context["worker"] = workers
        x = Worker.objects.all().values("contract_expiration_date")
        print(x)
        return context
