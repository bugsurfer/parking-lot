from constants.errors import errors
from models.car import Car
from models.parkinglot import ParkingLot


class ParkingLotHelper(object):
    def __init__(self):
        """
        Initializes a parking lot
        """
        self.parking_lot = None

    def create_parking_lot(self, size):
        """
        :return: Parking lot object
        Desc: Creates a parking lot with given size
        """
        self.parking_lot = ParkingLot(size)
        return self.parking_lot, 'Created a parking lot with {} slots'.format(size)

    def park_car(self, registration_number, color):
        """
        :param registration_number: Registration Number of the car
        :param color: Color of the car
        :return:

        Desc:
        1. Creates a car object with given details of the car
        2. Checks for the availability of the slot
        3. If available assigns the Slot and returns the associated slot number
        4. Else returns the error message
        """
        if not self.parking_lot.are_slots_available():
            # no slots are available i.e parking lot is full and cannot accomadate any more cars
            return errors.PARKING_LOT_IS_FULL

        if self.check_car_already_parked(registration_number=registration_number):
            return errors.CAR_ALREADY_PARKED

        car = Car(regnumber=registration_number, color=color)
        slot = self.parking_lot.get_available_slot()
        if not slot:
            return errors.PARKING_LOT_IS_FULL

        self.parking_lot.allocate_parking(car=car, slot=slot)
        return 'Allocated slot number: {}'.format(slot.slotNumber)

    def vacate_slot(self, slot_number):
        """
        :param slot_number: Slot Number to be evacuated
        :return:

        Desc:
        1. Updates Slot with empty car and and the occupied slots count
        """
        vacated_slot = self.parking_lot.vacate_slot(slot_number=slot_number)

        if not vacated_slot:
            return errors.UNAVAILABLE_SLOT

        return 'Slot number {} is free'.format(slot_number)

    def check_car_already_parked(self, registration_number):
        """
        :param registration_number: Registration Number of the car
        :return: returns True if car is already parked else False

        Desc: Assuming that car cannot be at the registration desk if the car is already parked inside
              or we can check the occupied slots of the parking lot with the given registration and color

              If it were a DB the Registration number would be the primary key
        """
        return False

    def parking_lot_status(self):
        """
        :return: Return the status of the Parking lot

        Desc:
        1. Get the occupied slots
        2. Get the cars parked in the slots and their details based on the maximum length the details of the slot + 4
        3. Adjusting the spaces
        """
        # print ('Slot No.    Registration No    Colour')
        max_slot_len = len("Slot No.")
        max_reg_no_length = len("Registration No")
        slots = self.parking_lot.slots
        parking_lot_status = []
        for slot_number, slot in slots.items():
            car = slot.get_occupied_car()
            if car:
                slot_number = str(slot_number)
                reg_no = car.get_registration_number()
                color = car.get_colour()
                if len(slot_number) > max_slot_len:
                    max_slot_len = len(slot_number)

                if len(reg_no) > max_reg_no_length:
                    max_reg_no_length = len(reg_no)
                parking_lot_status.append({'slot_number': slot_number, 'reg_no': reg_no, 'color': color})

        # printing status based on lengths
        max_slot_len = max_slot_len + 4
        max_reg_no_length = max_reg_no_length + 4

        return_string = ''
        return_string = return_string + 'Slot No.'.ljust(max_slot_len) + 'Registration No'.ljust(
            max_reg_no_length) + 'Colour' + '\n'
        for slot_details in parking_lot_status:
            slot_number = slot_details['slot_number']
            registration_number = slot_details['reg_no']
            color = slot_details['color']
            return_string = return_string + slot_number.ljust(max_slot_len) + registration_number.ljust(
                max_reg_no_length) + color + '\n'

        return return_string[:-1]

    def slots_numbers_for_cars_with_color(self, color):
        """
        :param color: Color of the Car
        :return: the slot numbers in which  cars of the given particular car are parked

        Desc:
        1. Get all the slots which are occupied
        2. Get the cars parked in these slots
        3. Get the cars details and slot numbers whose color is same as the given color
        """
        slot_numbers = []
        slots = self.parking_lot.slots
        for slot_number, slot in slots.items():
            car = slot.get_occupied_car()
            if car:
                if color == car.get_colour():
                    slot_numbers.append(str(slot_number))

        if not slot_numbers:
            return errors.NOT_FOUND

        slot_numbers_string = slot_numbers[0]
        for slot_number in slot_numbers[1:]:
            slot_numbers_string = slot_numbers_string + ', ' + slot_number

        return slot_numbers_string

    def registration_numbers_for_cars_with_color(self, color):
        """
        :param color: Color of the Car
        :return: Returns the registration numbers of the cars of this particular color which are parked
        """
        registration_numbers = []
        slots = self.parking_lot.slots
        for slot_number, slot in slots.items():
            car = slot.get_occupied_car()
            if car:
                if color == car.get_colour():
                    registration_numbers.append(car.get_registration_number())

        if not registration_numbers:
            return errors.NOT_FOUND

        registration_numbers_string = registration_numbers[0]
        for slot_number in registration_numbers[1:]:
            registration_numbers_string = registration_numbers_string + ', ' + slot_number

        return registration_numbers_string

    def slots_number_of_cars_with_registration_number(self, registration_number):
        """
        :param registration_number: Registration number of the car
        :return: Returns the slot in which the car is parked with the given registration number
        """
        slots = self.parking_lot.slots
        for slot_number, slot in slots.items():
            car = slot.get_occupied_car()
            if car:
                if registration_number == car.get_registration_number():
                    return slot_number

        return errors.NOT_FOUND
