from django_orion_model.fields import OrionCharField, OrionFloatField, OrionDateTimeField, OrionCoordinatesField
from django_orion_model.models import FamilyOrionEntity


class KeyPerformanceIndicator(FamilyOrionEntity):
    """Model of the key performance indicators"""
    FAMILY = "KeyPerformanceIndicator"

    name = OrionCharField(
        max_length=1024,
        help_text="Indicator's name which should be meaningful in the context of a project or organization. "
                  "Example `KPI-2016-2018-Incidences-Street`")
    alternateName = OrionCharField(
        max_length=1024, blank=True,
        help_text="An alias for the KPI")
    organization = OrionCharField(
        max_length=1024, blank=True,
        help_text="Subject organization evaluated by the KPI")
    process = OrionCharField(
        max_length=1024, blank=True,
        help_text="Subject process evaluated by the KPI")
    product = OrionCharField(
        max_length=1024, blank=True,
        help_text="Subject * product or service * evaluated by the KPI")
    provider = OrionCharField(
        max_length=1024, blank=True,
        help_text="Provider of the product or service, if any, that this KPI evaluates.")
    businessTarget = OrionCharField(
        max_length=1024, blank=True,
        help_text="For informative purposes, the business target to which this KPI is related to")
    description = OrionCharField(max_length=1024, blank=True, help_text="Indicator's description.")
    calculationFrequency = OrionCharField(
        max_length=1024, blank=True,
        help_text="How often the KPI is calculated.",
        choices=(
            ('hourly', 'hourly'),
            ('daily', 'daily'),
            ('weekly', 'weekly'),
            ('monthly', 'monthly'),
            ('yearly', 'yearly'),
            ('quarterly', 'quarterly'),
            ('bimonthly', 'bimonthly'),
            ('biweekly', 'biweekly'),))

    category = OrionCharField(
        max_length=1024, blank=True,
        help_text="Indicator's category.",
        choices=(
            ('quantitative', 'quantitative'),
            ('qualitative', 'qualitative'),
            ('leading', 'leading'),
            ('lagging', 'lagging'),
            ('input', 'input'),
            ('process', 'process'),
            ('output', 'output'),
            ('practical', 'practical'),
            ('directional', 'directional'),
            ('actionable', 'actionable'),
            ('financial', 'financial'),))
    calculatedBy = OrionCharField(
        max_length=1024, blank=True,
        help_text="The organization in charge of calculating the KPI")
    calculationMethod = OrionCharField(
        max_length=1024, blank=True,
        help_text="The calculation method used.")
    calculationFormula = OrionCharField(
        max_length=1024, blank=True,
        help_text="For informative purposes, the formula used for calculating the indicator")
    aggregatedData = OrionCharField(
        max_length=1024, blank=True,
        help_text="Entity(ies) and attribute(s) aggregated by the KPI.")
    calculationPeriod = OrionCharField(
        max_length=1024, blank=True,
        help_text="KPI 's period of time")
    currentStanding = OrionCharField(
        max_length=1024, blank=True,
        help_text="The KPI 's current standing as per its `kpiValue`. Values: very good, good, fair, bad, very bad.")
    kpiValue = OrionFloatField(
        help_text="Value of  the KPI.(Metadata: Units)")
    dateCreated = OrionDateTimeField(
        blank=True, null=True,
        help_text="The date on  which the organization created this KPI.This date might be different than the entity "
                  "creation date")
    referenceValue = OrionFloatField(
        blank=True, null=True,
        help_text="A reference this KPI should be similar to expectedValue")
    Expected = OrionFloatField(
        blank=True, null=True,
        help_text="value for the KPI according to the reference")
    desirableTendency = OrionCharField(
        max_length=1024, blank=True,
        help_text="A text describing the desirable tendency of the KPI.")
    dateNextCalculation = OrionDateTimeField(
        blank=True, null=True,
        help_text="Date on which a new  calculation of the KPI should be available.")
    dateExpires = OrionDateTimeField(
        blank=True, null=True,
        help_text="The date on which the KPI  will be no longer necessary or meaningful")
    dateModified = OrionDateTimeField(
        blank=True, null=True,
        help_text="Last update date of the KPI data.This can be different than the last update date of the KPI's value")
    location = OrionCoordinatesField(
        blank=True, null=True,
        help_text="Location of the area to which the KPI refers to")
    address = OrionCharField(
        max_length=1024, blank=True,
        help_text="Civic address of the area to which the KPI refers to")
    area = OrionCharField(
        max_length=1024, blank=True,
        help_text="For organizational purposes, it allows to add extra textual geographical information such as "
                  "district, borough, or any other hint which can help to identify the KPI coverage.")


class ZKPI(KeyPerformanceIndicator):
    pass
