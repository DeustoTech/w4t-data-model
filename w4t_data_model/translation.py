from modeltranslation.translator import register, TranslationOptions

from w4t_data_model.models import ResourceCategory
from w4t_data_model.models.entities import ResourceCollection
from w4t_data_model.models.waste_characterizations import Resource, TranslatedWaste, TranslatedWasteCategory, \
    TranslatedSortingType


@register(Resource)
class ResourceTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(ResourceCategory)
class ResourceTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(ResourceCollection)
class ResourceTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(TranslatedWaste)
class WasteTranslationOptions(TranslationOptions):
    fields = ()


@register(TranslatedWasteCategory)
class WasteCategoryTranslationOptions(TranslationOptions):
    fields = ()


@register(TranslatedSortingType)
class SortingTypeTranslationOptions(TranslationOptions):
    fields = ()
