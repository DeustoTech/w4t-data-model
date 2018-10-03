from django.contrib import admin
from w4t_waste_collection.models.waste_characterizations import Waste, WasteCategory, SortingType, WasteManagementStage


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