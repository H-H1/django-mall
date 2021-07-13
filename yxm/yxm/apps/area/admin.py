from django.contrib import admin

# Register your models here.
import xadmin
from area.models import Area

xadmin.site.register(Area)