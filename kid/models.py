from __future__ import unicode_literals

from django.db import models


class Qingyang(models.Model):
    field_area = models.CharField(db_column='\ufeffarea', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    no = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=False,primary_key = True)
    address = models.CharField(max_length=255, blank=True, null=True)
    whether_public_welfare = models.CharField(db_column='Whether public welfare', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nature = models.CharField(max_length=255, blank=True, null=True)
    grade = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    lng = models.CharField(max_length=255, blank=True, null=True)
    lat = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return '%s,%s'%(self.lng,self.lat)
    class Meta:
        managed = False
        db_table = 'qingyang'