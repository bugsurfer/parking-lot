from models.slot import Slot


class ParkingLot(object):
    """
    Class for parkingLot
    """

    def __init__(self, size):
        """
        :param size: No of parking lots in total
        Desc: Creates n no of slots based on the size given
        """
        slots = {}
        for i in range(1, size + 1):
            slots[i] = Slot(slot_number=i)

        self.slots = slots
        self.totalSlots = size
        self.occupied_slots_count = 0

    def are_slots_available(self):
        """
        :return: return True if slots are available else False
        """
        return not self.occupied_slots_count == self.totalSlots

    def get_available_slot(self):
        """
        :return: Return the first available slot
        """
        for slot_number, slot in self.slots.items():
            if not slot.get_occupied_car():
                return slot

        return None

    def allocate_parking(self, car, slot):
        """
        :param car: Car to be parked
        :param slot: Slot to be allocated
        :return: None

        Desc: Allocates the car to the given Slot and increases the occupied slots count
        """
        self.occupied_slots_count = self.occupied_slots_count + 1
        slot.allocate_car(car=car)

    def get_occupied_slots_count(self):
        """
        :return: Return Occupied slots Count
        """
        return self.occupied_slots_count

    def vacate_slot(self, slot_number):
        """
        :param slot_number: Slot to be vacte
        :return: return the vacated slot
        """
        slot = self.slots.get(slot_number)
        if slot and slot.get_occupied_car():
            self.occupied_slots_count = self.occupied_slots_count - 1
            slot.vacate_slot()
            return slot

        return slot

    def get_total_slots(self):
        """
        :return: Returns total number of slots available in Parking Lot
        """
        return self.totalSlots
