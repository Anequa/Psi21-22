from django.urls import path
from shelter.views import HomePageView

urlpatterns = [path("", HomePageView.as_view(), name="home_page")]
