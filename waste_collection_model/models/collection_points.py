""" Models to manage the Waste Collection points
"""

from django_orion_model.models import OrionEntity, OrionCharField, OrionTextField, OrionFloatField, OrionDateTimeField
from django.db.models import ForeignKey


class CollectionPointType(OrionEntity):

    class Meta:
        """ This made available to declare model in models package instead of models.py"""
        app_label = 'waste_collection_model'

    """Model of the collection point that determine common properties of some collection point"""
    name = OrionCharField("name")
    description = OrionTextField("description")
    # description = models.TextField(blank=True)
    # width = models.FloatField(blank=True)
    # width_meta = models.CharField(blank=True)
    # height = models.FloatField(blank=True)
    # height_meta = models.CharField(blank=True)
    # deep = models.FloatField(blank=True)
    # deep_meta = models.CharField(blank=True)
    # weight = models.FloatField(blank=True)
    # weight_meta = models.CharField(blank=True)
    # cargoVolume = models.FloatField(blank=True)
    # cargoVolume_meta = models.CharField(blank=True)
    # maximumLoad = models.FloatField(blank=True)
    # maximumLoad_meta = models.CharField(blank=True)
    # recommendedLoad = models.FloatField(blank=True)
    # recommendedLoad_meta = models.CharField(blank=True)
    # category = models.TextField()
    # insertHoleNumber = models.IntegerField(blank=True)
    # insertHoleWidth = models.FloatField(blank=True)
    # loadType = models.CharField(blank=True)
    # madeOf = models.TextField(blank=True)
    # madeOfCodes = models.CharField(blank=True)
    # brandName = models.CharField(blank=True)
    # modelName = models.CharField(blank=True)
    # manufacturerName = models.CharField(blank=True)
    # colors = models.CharField(blank=True)
    # image = models.URLField(blank=True)
    # compliantWith = models.CharField(blank=True)
    # accessLimitation = models.CharField(blank=True)
    # userIdentification = models.CharField(blank=True)
    # inputControl = models.CharField(blank=True)
    # maximumInputVolume = models.FloatField(blank=True)
    # maximumInputVolume_meta = models.CharField(blank=True)
    # features = models.TextField(blank=True)
#
#
# class CollectionPointIsle(models.Model):
#     """ A set of collection points that are so close that """
#
#     description = models.TextField(blank=True)
#
#     @property
#     def refCollectionPoints(self):
#         return self.collectionpoint_set.all()
#
#     # GeoPoint
#     location = models.CharField()
#     features = models.TextField(blank=True)
#     address = models.TextField(blank=True)
#     areaServed = models.CharField(blank=True)
#
#     dateModified = models.DateField(blank=True)
#     dateCreated = models.DateField(blank=True)
#
#
# class CollectionPoint(models.Model):
#     """A source of Waste."""
#
#     id = models.TextField(unique=True)
#
#     refCollectionPointType = models.ForeignKey(CollectionPointType, on_delete=models.SET_NULL)
#     refCollectionPointIsle = models.ForeignKey(CollectionPointIsle, on_delete=models.SET_NULL, blank=True)
#     refSortingType = models.ForeignKey(SortingType, on_delete=models.SET_NULL)
#
#     serialNumber = models.CharField()
#     refDevice = models.CharField(blank=True)
#
#     description = models.TextField(blank=True)
#
#     storedWasteOrigin = models.CharField(blank=True)
#     # GeoPoint
#     location = models.CharField()
#     address = models.TextField(blank=True)
#     fillingLevel = models.DecimalField(max_digits=2, decimal_places=1, blank=True)
#     # Meta??
#     cargoWeight = models.FloatField(blank=True)
#     temperature = models.DecimalField(blank=True)
#     methaneConcentration = models.FloatField(blank=True)
#     regulations = models.CharField(blank=True)
#     responsible = models.CharField()
#     owner = models.CharField()
#     dateServiceStarted = models.TimeField(blank=True)
#     dateLastEmptying = models.TimeField(blank=True)
#     nextActuationDeadline = models.TimeField(blank=True)
#     # http://schema.org/openingHours
#     actuationHours = models.CharField(blank=True)
#     openingHours = models.CharField(blank=True)
#     dateLastCleaning = models.TimeField(blank=True)
#     nextCleaningDeadline = models.TimeField(blank=True)
#
#     status = models.CharField(blank=True)
#     color = models.CharField(blank=True)
#     image = models.URLField(blank=True)
#     annotations = models.TextField(blank=True)
#     areaServed = models.CharField(blank=True)
#     dateModified = models.DateField(blank=True)
