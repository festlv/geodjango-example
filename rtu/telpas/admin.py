from django.contrib.gis import admin
from telpas.models import Eka, Telpa

admin.site.register(Eka, admin.GeoModelAdmin)
admin.site.register(Telpa, admin.GeoModelAdmin)
