""" Models to manage the Waste elements
"""
from w4t_data_model.models.entities import Resource, ResourceCategory, ResourceCollection
from django_orion_model.models.fields import OrionCharField, OrionTextField, OrionJSONField, OrionDateTimeField
# TODO Name Translation see https://django-modeltranslation.readthedocs.io/en/latest/installation.html#setup


class Waste(Resource):
    wasteCode = OrionCharField(
        max_length=1024, blank=True,
        help_text="LER waste code.")
    definitionSource = OrionTextField(
        blank=True,
        help_text="Where this characterization comes from")


class WasteCategory(ResourceCategory):
    pass


class SortingType(ResourceCollection):

    shape = OrionCharField(
        max_length=1024, blank=True,
        help_text="If the shape of the container is very relevant or representative for the sorting type (mainly for "
                  "the sorting game) specify the shape of the container. Accepted values: the shapes provided by the "
                  "sorting game.")
    color = OrionCharField(
        max_length=1024, blank=True,
        help_text="Sorting type's associated color. Example 'Green'")
    annotations = OrionTextField(
        max_length=1024, blank=True,
        help_text="Attribute reserved for annotations (incidences, remarks, etc.)")
    wasteCharacterization = OrionJSONField(
        blank=True, null=True,
        help_text="{wasteCategory_X : {amount: X, unit: KGM}, WasteCategory_Y : {amount: Y, unit: KGM}...}...}")
    wasteCharacterizationTime = OrionDateTimeField(
        blank=True,
        help_text="Timestamp at which the wasteCharacterization field was updated")
    area_served = OrionCharField(
        max_length=1024, blank=True,
        help_text="Higher level area to which the sorting type belongs to. It can be used to define the "
                  "area where the sorting type is applied, etc.")
