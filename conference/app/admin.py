from django.contrib import admin
# Register your models here.
from .models import *
admin.site.register(Speaker)
admin.site.register(session)
admin.site.register(Visitor)
admin.site.register(Vcount)
