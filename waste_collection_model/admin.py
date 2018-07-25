from django.contrib import admin
from django.contrib.postgres import fields
from django_json_widget.widgets import JSONEditorWidget


from waste_collection_model.models.waste_characterizations import Waste, WasteCategory, SortingType, WasteManagementStage


@admin.register(Waste)
class StrategyAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'waste_code')


@admin.register(WasteCategory)
class StrategyAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(SortingType)
class StrategyAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'regulation', 'color', 'annotations', 'area_served')


@admin.register(WasteManagementStage)
class WasteManagementStageAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')