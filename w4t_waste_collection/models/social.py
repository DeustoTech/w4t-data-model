from django.utils.safestring import SafeString

from django_orion_model.fields import OrionCharField, OrionTextField, OrionDecimalField, \
    OrionDateTimeField, OrionBooleanField, OrionRef, OrionRefList, OrionURLField, OrionIntegerField
from django_orion_model.models import OrionEntity


class Action(OrionEntity):
    refStrategy = OrionRef(help_text="")
    name = OrionCharField(max_length=1024, help_text="")
    description = OrionTextField(help_text="")
    status = OrionCharField(max_length=1024, help_text="")
    startDate = OrionDateTimeField(help_text="")
    endDate = OrionDateTimeField(help_text="")
    areaServed = OrionCharField(max_length=1024, help_text="")
    areaDescription = OrionCharField(max_length=1024, help_text="")
    communicationTools = OrionCharField(max_length=1024, help_text="")
    costs = OrionDecimalField(max_digits=10, decimal_places=2, help_text="", )
    economicalImpact = OrionDecimalField(max_digits=10, decimal_places=2, help_text="")
    environmentalImpact = OrionTextField(help_text="")
    otherImpact = OrionTextField(help_text="")
    isBestPractice = OrionBooleanField(help_text="")
    lessonsLearnt = OrionTextField(help_text="")
    monitoringMethodology = OrionTextField(help_text="")
    otherInformation = OrionTextField(help_text="")
    otherTools = OrionTextField(help_text="")
    socialImpact = OrionTextField(help_text="")
    successKeyPoints = OrionTextField(help_text="")
    trainingTools = OrionTextField(help_text="")
    refWasteStages = OrionRef(help_text="")
    refWasteStreams = OrionRefList(help_text="")
    url = OrionURLField()

    @property
    def url_link(self):
        return SafeString('<a href="' + self.url + '" >View</a>')

    @property
    def strategy(self):
        strategies = {
            "1": "General sensitization Campaign",
            "2": "Education Centers Actions",
            "3": "Food Waste Prevention Campaign",

            "4": "Commercial Activities Campaign",
            "5": "Composting",
            "6": "PAYT",
            "7": "Zero Waste Ecosystems",
            "23": "Zero Waste Events",
            "8": "Miscellaneous"
        }
        
        return strategies[self.refStrategy.split(":")[1]]


class Strategy(OrionEntity):
    name = OrionCharField(max_length=1024)
    description = OrionTextField()
    startDate = OrionDateTimeField()
    endDate = OrionDateTimeField()
    executor = OrionCharField(max_length=1024)
    keyMessages = OrionTextField()
    monitoringStrategy = OrionTextField()
    promoter = OrionCharField(max_length=1024)
    url = OrionURLField()
    refActions = OrionRefList()
    refTargetGroups = OrionRefList()
    refWasteStages = OrionRefList()
    refWasteStreams = OrionRefList()
    resultsFeedback = OrionTextField()


class SortingGameUserMetrics(OrionEntity):

    age = OrionIntegerField()
    allTimeLevelsPlayed = OrionIntegerField()
    countryISO = OrionCharField(max_length=10)
    currentMaxLevel = OrionIntegerField()
    currentTotalPoints = OrionIntegerField()
    gender = OrionCharField(max_length=10)
    latestLevelPlayed = OrionIntegerField()
    municipalityName = OrionCharField(max_length=50)




