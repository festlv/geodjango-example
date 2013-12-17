from django.contrib.gis.db import models


class Eka(models.Model):
    iela = models.CharField(max_length=255)
    pilseta = models.CharField(max_length=255)
    lat = models.FloatField()
    lon = models.FloatField()

    kontura = models.MultiPolygonField()
    objects = models.GeoManager()

    def __unicode__(self):
        return "Eka: %d" % (self.pk, )


class Telpa(models.Model):
    eka = models.ForeignKey(Eka)
    stavs = models.IntegerField()
    numurs = models.IntegerField()
    kontura = models.MultiPolygonField()

    objects = models.GeoManager()

    def __unicode__(self):
        return "Telpa: %d" % (self.pk, )
