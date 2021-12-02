from django.contrib import admin

from .models import User, Worker

# from django.forms.models import ModelChoiceField


# Register your models here.
# class UserAdmin(admin.ModelAdmin):
#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         if db_field.name == "username":
#             if request.user.is_superuser:
#                 print("welcome")
#                 workers = Worker.objects.all().values("username")
#                 workers = [w["username"] for w in workers]
#                 users = User.objects.all().values("username")
#                 users = [u["username"] for u in users]
#                 usernames = [user for user in users if user not in workers]
#                 queryset = User.objects.filter(username__in=usernames)
#                 return ModelChoiceField(queryset, initial=request.user)
#         else:
#             print("jest else")


admin.site.register(User)
admin.site.register(Worker)
