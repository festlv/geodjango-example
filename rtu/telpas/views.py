from django.shortcuts import render
from vectorformats.Formats import Django, GeoJSON
from django.utils.safestring import mark_safe

from telpas.models import Eka

def index(request):
    qs = Eka.objects.all()
    djf = Django.Django(geodjango="kontura", properties=['lat', 'lon'])
    geoj = GeoJSON.GeoJSON()
    s = geoj.encode(djf.decode(qs))
    data = {'geojson':  mark_safe(s)}

    return render(request, 'telpas/index.html', data)
