from w4t_waste_collection.models.entities import Agent, AgentType, Transaction


class TreatmentPlant(Agent):
    pass


class TreatmentPlantType(AgentType):
    pass


class WasteTransaction(Transaction):
    """ Waste movements."""
    additional_fields = ["received_sum", "emitted_sum"]

    @property
    def received_sum(self):
        """Add all amounts of received resources. """
        return sum(resource["amount"] for resource in self.receivedResources)

    @property
    def emitted_sum(self):
        """Add all amounts of emitted resources. """
        return sum(resource["amount"] for resource in self. emittedResources)
