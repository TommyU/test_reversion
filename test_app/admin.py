from django.contrib import admin
import reversion
from .models import article
# Register your models here.
class articleAdmin(reversion.VersionAdmin):#reversion.VersionAdmin#admin.ModelAdmin
    list_display = ("id", "title", "author", "status","create_date")

admin.site.register(article,articleAdmin)

