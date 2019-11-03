class Car(object):
    """
    Class for Car
    """

    def __init__(self, regnumber, color):
        """
        :param regnumber: Registration Number of the Car
        :param color: Color of the Car
        Desc: Initializes a car object with the given registration number and color
        """
        self.registrationNumber = regnumber
        self.color = color
        self.slot = None

    def set_slot(self, slot):
        """
        :param slot: Slot Object
        :return: None
        Desc: Sets the car's slot to the given slot
        """
        if not self.slot:
            self.slot = slot
        else:
            raise Exception('Slot is already Allocated')

    def get_slot(self):
        """
        :return: Return's the slot object
        """
        return self.slot

    def get_colour(self):
        """
        :return: Return's the car color
        """
        return self.color

    def get_registration_number(self):
        """
        :return: Returns the Car's registration Number
        """
        return self.registrationNumber
