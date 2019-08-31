from django_orion_model.models.entities import FamilyOrionEntity
from django_orion_model.models.fields import OrionCoordinatesField, OrionTextField, OrionCharField, OrionRef, \
    OrionRefList, OrionDateTimeField, OrionListField


class Agent(FamilyOrionEntity):
    """Each instance where waste is created, transformed or consumed, belonging to a WasteEntityType and containing the
    location of the entity together with specific features"""
    FAMILY = "Agent"

    location = OrionCoordinatesField(blank=True)
    address = OrionTextField(blank=True)
    name = OrionCharField(max_length=1024)
    refType = OrionRef()
    refInputs = OrionRefList(null=True)
    refOutputs = OrionRefList(null=True)
    refAgentCollection = OrionRef(null=True)
    # Not included any optional attributes define them into subclasses

    class Meta:
        abstract = True


class AgentType(FamilyOrionEntity):
    FAMILY = "AgentType"

    name = OrionCharField(max_length=1024)
    refInputs = OrionRefList()
    refOutputs = OrionRefList()

    class Meta:
        abstract = True


class AgentCollection(FamilyOrionEntity):
    FAMILY = "AgentCollection"


class Transaction(FamilyOrionEntity):
    FAMILY = "Transaction"

    refEmitter = OrionRef(
        blank=True,
        help_text="Transaction's emitter entity containing an Agent ID.")
    refReceiver = OrionRef(
        help_text="Transaction's receiver entity containing an Agent ID.")
    refCapturer = OrionRef(
        blank=True,
        help_text="Reference to the Id of the Device entity if exists, that captured the transaction containing an "
                  "Agent ID..")
    date = OrionDateTimeField(
        help_text="Timestamp which represents when the transaction was made")
    emittedResources = OrionListField(
        help_text="JSON ARRAY [{ refResource : resourceID_X , amount : amount1 , unit : ""KGM"" , ...},{ refResource : "
                  "resourceID_X , amount : amount2 , unit : ""KGM"" , ... },... ]")
    receivedResources = OrionListField(
        help_text="JSON ARRAY [{ refResource : resourceID_X , amount : amount1 , unit : 'KGM' , ... },"
                  "{ refResource : resourceID_X , amount : amount2 , unit :'KGM' , ... },... ]")
    incorrect = OrionDateTimeField(
        blank=True, null=True,
        help_text="Default to null or nor existing. In order not to delete any transaction, If one is incorrect to mark"
                  " it as incorrect and do not use it in calculations. But keep it in the database to know.")
    incorrectReason = OrionTextField(
        blank=True,
        help_text="Explanation if necessary of what it is incorrect or what changes have been handmade.For example: "
                  "'Bad transaction because of sensor error"" , ""refEmitter has been manually changed from citizen:31 "
                  "to citizen:523' , etc")


class Resource(FamilyOrionEntity):
    FAMILY = "Resource"

    name = OrionCharField(
        max_length=1024,
        help_text="Waste Name. Example 'Green glass bottle'")

    description = OrionTextField(
        help_text="Waste help_text. Example 'Bottle made of green glass'", blank=True)

    refCategory = OrionRef(
        help_text="Reference to category entity this belongs. Example [wastecategory:9[]")


class ResourceCategory(FamilyOrionEntity):
    FAMILY = "ResourceCategory"

    name = OrionCharField(
        max_length=1024, blank=True,
        help_text="WasteCategory Name. Example 'Glass bottles'", )

    description = OrionTextField(
        max_length=1024, blank=True,
        help_text="WasteCategory description. Example 'Glass bottles including whiteand green glass'")

    ref_resources = OrionRefList(
        help_text="List of waste entities composing the ResourceCategory. Example [waste:6, waste:18]")


class ResourceCollection(FamilyOrionEntity):
    FAMILY = "ResourceCollection"

    name = OrionCharField(max_length=1024, blank=True,
                          help_text="SortingType Name. Example 'Color Glass collection'")
    description = OrionTextField(max_length=1024, blank=True,
                                 help_text="SortingType description. Example 'Collection of colored glass bottles'")

    regulation = OrionCharField(
        max_length=1024, blank=True)
    refResources = OrionRefList(
        help_text="List of waste entities composing the SortingType. Example [waste:6, waste18]")
