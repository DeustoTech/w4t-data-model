from django.utils.safestring import SafeString

from django_orion_model.models.fields import OrionCharField, OrionTextField, OrionDecimalField, \
    OrionDateTimeField, OrionBooleanField, OrionRef, OrionRefList, OrionURLField
from django_orion_model.models.entities import OrionEntity


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

            "8": "Miscellaneous",
            "9": "Citizens' Sensitization - Funny Door to Door Sensitization",
            "10": "Zero Waste Campaigns -Virtuous Households",
            "11": "Zero Waste Events",
            "12": "PAYT Introduction - Communication",
            "13": "Promotion Campaign of Reusable Nappies",
            "14": "Reusable Nappies Campaign - Nursery Schools",

            "15": "Educational Centers Activities",
            "16": "Actions at Technical University",
            "17": "Food Separate Collection and Treatment",
            "18": "Commercial Activities Campaign",
            "19": "Collection of Nappies",
            "20": "ID/PAYT Containers System",
            "21": "Tourist Engagement",
            "22": "Waste4Think Schools",
            "23": "Zero Waste Events",
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
