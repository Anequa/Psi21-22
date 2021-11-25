# from django.http import HttpResponse
# from django.shortcuts import render
from authentication.models import User, Worker
from django.views.generic import TemplateView

# def first_view(request):
#     return HttpResponse("first view")


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        workers = Worker.objects.all().values("username")
        workers = [w["username"] for w in workers]
        users = User.objects.all().values("username")
        users = [u["username"] for u in users]
        usernames = [user for user in users if user not in workers]
        context["workers"] = workers
        context["users"] = users
        context["username"] = usernames
        context["x"] = User.objects.filter(username__in=usernames)
        return context
