""" Models to manage the Waste elements
"""

from django_orion_model.models import OrionEntity, OrionCharField, OrionTextField, OrionFloatField, OrionDateTimeField
from django.db.models import ForeignKey

# class WasteCategory(models.Model):
#     id = models.TextField(unique=True)
#     name = models.CharField()
#     description = models.TextField(blank=True)
#
#     @property
#     def refWastes(self):
#         self.waste_set.all()
#         return None
#
#
# class Waste(models.Model):
#     id = models.TextField(unique=True)
#     name = models.CharField()
#     description = models.TextField(blank=True)
#     wasteCode = models.CharField()
#     refWasteCategory = models.ForeignKey(WasteCategory, on_delete=models.SET_NULL)
#
#
# class SortingType(models.Model):
#     id = models.TextField(unique=True)
#     name = models.CharField()
#     description = models.TextField(blank=True)
#     regulation = models.CharField(blank=True)
#     color = models.CharField(blank=True)
#     annotations = models.TextField(blank=True)
#     areaServed = models.CharField(blank=True)
#     refWastes = models.ManyToManyField(Waste)
