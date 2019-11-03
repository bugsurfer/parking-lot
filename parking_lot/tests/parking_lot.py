import os
import sys
import unittest

sys.path.insert(0, os.path.abspath('../'))

from constants.errors import errors
from services.parking_lot_helper import ParkingLotHelper


class testSuites(unittest.TestCase):
    """
    Test Cases
    """

    def setUp(self):
        self.parking_lot_helper = ParkingLotHelper()
        self.parking_lot, status = self.parking_lot_helper.create_parking_lot(size=2)

    def test_create_parking_lot(self):
        self.assertEqual(self.parking_lot.get_total_slots(), 2)

    def test_park_car(self):
        return_string = self.parking_lot_helper.park_car('ABCD', 'Grey')
        self.assertEqual('Allocated slot number: 1', return_string)
        return_string = self.parking_lot_helper.park_car('ABCDE', 'Grey')
        self.assertEqual('Allocated slot number: 2', return_string)

    def test_leave_slot(self):
        self.parking_lot_helper.park_car('ABC', 'Grey')
        self.parking_lot_helper.park_car('ABCD', 'Grey')
        return_string = self.parking_lot_helper.vacate_slot(1)
        self.assertEqual('Slot number 1 is free', return_string)

    def test_if_parking_lot_is_full(self):
        self.parking_lot_helper.park_car('ABC', 'Grey')
        self.parking_lot_helper.park_car('ABCD', 'Grey')
        return_string = self.parking_lot_helper.park_car('ABCDE', 'Grey')
        self.assertEqual(errors.PARKING_LOT_IS_FULL, return_string)

    def test_parking_lot_status(self):
        self.parking_lot_helper.park_car('ABC', 'Grey')
        status = self.parking_lot_helper.parking_lot_status()
        expected_status = 'Slot No.    Registration No    Colour\n1           ABC                Grey'
        self.assertEqual(expected_status, status)

    def test_slot_numbers_for_cars_with_colour(self):
        self.parking_lot_helper.park_car('ABC', 'Grey')
        self.parking_lot_helper.park_car('ABCD', 'White')
        self.assertEqual('1', self.parking_lot_helper.slots_numbers_for_cars_with_color(color='Grey'))

        self.parking_lot_helper.vacate_slot(2)
        self.parking_lot_helper.park_car('ABCD', 'Grey')
        self.assertEqual('1, 2', self.parking_lot_helper.slots_numbers_for_cars_with_color(color='Grey'))

        self.parking_lot_helper.vacate_slot(2)
        self.parking_lot_helper.vacate_slot(1)

        self.assertEqual(errors.NOT_FOUND, self.parking_lot_helper.slots_numbers_for_cars_with_color(color='Grey'))

    def test_registration_numbers_for_cars_with_colour(self):
        self.parking_lot_helper.park_car('ABC', 'Grey')
        self.parking_lot_helper.park_car('ABCD', 'White')
        self.assertEqual('ABC', self.parking_lot_helper.registration_numbers_for_cars_with_color(color='Grey'))

        self.parking_lot_helper.vacate_slot(2)
        self.parking_lot_helper.park_car('ABCD', 'Grey')
        self.assertEqual('ABC, ABCD', self.parking_lot_helper.registration_numbers_for_cars_with_color(color='Grey'))

        self.parking_lot_helper.vacate_slot(2)
        self.parking_lot_helper.vacate_slot(1)

        self.assertEqual(errors.NOT_FOUND, self.parking_lot_helper.registration_numbers_for_cars_with_color(color='Grey'))

    def test_slot_number_for_registration_number(self):
        self.parking_lot_helper.park_car('ABC', 'Grey')
        self.parking_lot_helper.park_car('ABCD', 'White')

        self.assertEqual(1, self.parking_lot_helper.slots_number_of_cars_with_registration_number(registration_number='ABC'))

        self.assertEqual(errors.NOT_FOUND, self.parking_lot_helper.slots_number_of_cars_with_registration_number(registration_number='ABCDEF'))


if __name__ == '__main__':
    unittest.main()
