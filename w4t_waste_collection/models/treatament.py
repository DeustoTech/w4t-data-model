from w4t_waste_collection.models.entities import Agent, AgentType, Transaction


class TreatmentPlant(Agent):
    pass


class TreatmentPlantType(AgentType):
    pass


class WasteTransaction(Transaction):
    """ Waste movements."""
    additional_fields = ["received_sum", "emitted_sum"]

    @property
    def biowaste_sum(self):
        """Add all amounts of received resources. """
        return sum(
            resource["amount"]
            for resource in self.receivedResources
            if resource["refResource"] in ["Resource:fruits_vegetables", "Resource:edible_starchy", "Resource:edible_animal"]
        )

    @property
    def nappies_sum(self):
        """Add all amounts of received resources. """
        return sum(
            resource["amount"]
            for resource in self.receivedResources
            if resource["refResource"] in ["Resource:infant_nappies", "Resource:adult_nappies"]
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
            if resource["refResource"] in ["Resource:hfw", ]
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