""" Models to manage the Waste elements
"""
from django_orion_model.models import OrionEntity, OrionCharField, OrionTextField, OrionFloatField, OrionDateTimeField
from django.db.models import ForeignKey, ManyToManyField, SET_NULL


class WasteManagementStage(OrionEntity):

    class Meta:
        """ This made available to declare model in models package instead of models.py"""
        app_label = 'w4t_waste_collection'

    name = OrionCharField("name", max_length=1024, blank=True)
    description = OrionTextField("description", max_length=1024, blank=True)

    def __str__(self):
        return '{0}:{1} {2}'.format(self.orion_type, self.orion_id, self.name)


class WasteCategory(OrionEntity):

    class Meta:
        """ This made available to declare model in models package instead of models.py"""
        app_label = 'w4t_waste_collection'

    name = OrionCharField("name", max_length=1024, blank=True)
    description = OrionTextField("description", max_length=1024, blank=True)

    @property
    def refWastes(self):
        self.waste_set.all()
        return None

    def __str__(self):
        return '{0}:{1} {2}'.format(self.orion_type, self.orion_id, self.name)


class Waste(OrionEntity):

    class Meta:
        """ This made available to declare model in models package instead of models.py"""
        app_label = 'w4t_waste_collection'

    name = OrionCharField("name", max_length=1024, blank=True)
    description = OrionTextField("description", max_length=1024, blank=True)
    waste_code = OrionCharField("wasteCode", max_length=1024, blank=True)
    ref_waste_category = ForeignKey(WasteCategory, blank=True, null=True, on_delete=SET_NULL )

    def __str__(self):
        return '{0}:{1} {2}'.format(self.orion_type, self.orion_id, self.name)


class SortingType(OrionEntity):

    class Meta:
        """ This made available to declare model in models package instead of models.py"""
        app_label = 'w4t_waste_collection'

    name = OrionCharField("name", max_length=1024, blank=True)
    description = OrionTextField("description", max_length=1024, blank=True)
    regulation = OrionCharField("regulation", max_length=1024, blank=True)
    color = OrionCharField("color", max_length=1024, blank=True)
    annotations = OrionTextField("annotations", max_length=1024, blank=True)
    area_served = OrionCharField("areaServed", max_length=1024, blank=True)
    ref_wastes = ManyToManyField(Waste)

    def __str__(self):
        return '{0}:{1} {2}'.format(self.orion_type, self.orion_id, self.name)


