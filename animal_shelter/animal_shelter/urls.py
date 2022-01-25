from decorator_include import decorator_include
from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("shelter/", include("shelter.urls")),
    path("api/", decorator_include(staff_member_required, "api.urls")),
    path("api-auth/", include("rest_framework.urls")),
]
