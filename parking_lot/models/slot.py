class Slot(object):
    """
    Class for Slot
    """

    def __init__(self, slot_number):
        """
        :param slot_number: Slot Number to be assigned
        """
        self.slotNumber = slot_number
        self.car = None

    def get_slot_number(self):
        """
        :param self:
        :return: Returns the slot number associated with the particular slot
        """
        return self.slotNumber

    def is_available(self):
        """
        :return: Return if slot is available
        """
        if self.car:
            return False
        return True

    def get_occupied_car(self):
        """
        :return: Returns the car occupied in the particular slot
        """
        return self.car

    def allocate_car(self, car):
        """
        :param car: Car Object
        :return: Allocates the Slot to the given Car
        """
        self.car = car

    def vacate_slot(self):
        """
        :return: Vacates the Slot
        """
        self.car = None
