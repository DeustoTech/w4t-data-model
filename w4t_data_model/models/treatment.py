from w4t_data_model.models.entities import Agent, AgentType, Transaction


class TreatmentPlant(Agent):
    ORION_TYPE = "TreatmentPlant"


class TreatmentPlantType(AgentType):
    ORION_TYPE = "TreatmentPlantType"


class WasteTransaction(Transaction):
    """ Waste movements."""
    additional_fields = ["received_sum", "emitted_sum"]
    ORION_TYPE = "WasteTransaction"

    @property
    def biowaste_sum(self):
        """Add all amounts of received resources. """
        return sum(
            resource["amount"]
            for resource in self.receivedResources
            if resource["refResource"] in
            ["Waste:129", "Waste:957", "Waste:73"]
        )

    @property
    def nappies_sum(self):
        """Add all amounts of received resources. """
        return sum(
            resource["amount"]
            for resource in self.receivedResources
            if resource["refResource"] in ["Waste:955", "Waste:956"]
        )

    @property
    def compost_sum(self):
        """Add all amounts of received resources. """
        return sum(
            resource["amount"]
            for resource in self.emittedResources
            if resource["refResource"] in ["Resource:compost", ]
        )

    @property
    def biogas_stp_sum(self):
        """Add all amounts of received resources. """
        return sum(
            resource["amount"]
            for resource in self.emittedResources
            if resource["refResource"] in ["Resource:biogas_stp", ]
        )

    @property
    def hfw_sum(self):
        """Add all amounts of received resources. """
        return sum(
            resource["amount"]
            for resource in self.receivedResources
            if resource["refResource"] in ["Waste:958", ]
        )

    @property
    def energy_consumption_sum(self):
        """Add all amounts of received resources. """
        return sum(
            resource["amount"]
            for resource in self.receivedResources
            if resource["refResource"] in ["Resource:energy_consumption", ]
        )

    @property
    def forbi_sum(self):
        """Add all amounts of received resources. """
        return sum(
            resource["amount"]
            for resource in self.emittedResources
            if resource["refResource"] in ["Resource:forbi", ]
        )

    @property
    def dry_organic(self):
        """Add all amounts of received resources. """
        return sum(
            resource["amount"]
            for resource in self.receivedResources
            if resource["refResource"] in ["SortingType:10", ]
        )

    @property
    def wet_organic(self):
        """Add all amounts of received resources. """
        return sum(
            resource["amount"]
            for resource in self.receivedResources
            if resource["refResource"] in ["SortingType:10", ]
        )
