from django.contrib import admin
from .models import Register
from .models import Houses
from . models import Payments, Notices

# Register your models here.
admin.site.register(Register)
admin.site.register(Houses)
admin.site.register(Payments)
admin.site.register(Notices)
