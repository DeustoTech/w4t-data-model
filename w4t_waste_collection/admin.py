from django.contrib import admin
from w4t_waste_collection.models.waste_characterizations import Resource, ResourceCategory, SortingType


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    pass


@admin.register(ResourceCategory)
class ResourceCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(SortingType)
class SortingTypeAdmin(admin.ModelAdmin):
    pass
