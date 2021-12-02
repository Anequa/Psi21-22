from django.contrib import admin

from .models import Adoption, Animal, Cage, Photo, Reservation

# Register your models here.
admin.site.register(Animal)
admin.site.register(Photo)
admin.site.register(Cage)
admin.site.register(Reservation)
admin.site.register(Adoption)
