import sys

from constants.commands import *
from constants.errors import errors
from services.parking_lot_helper import ParkingLotHelper

parking_lot = None
parking_lot_helper = ParkingLotHelper()


def run_query(query):
    query_params = query.split()

    command = query_params[0]
    if command not in ALL_COMMANDS:
        print(errors.INVALID_COMMAND)

    if command == CREATE_PARKING_LOT:
        size = query_params[1]
        global parking_lot
        parking_lot, status = parking_lot_helper.create_parking_lot(size=int(size))
        print(status)
    else:
        if not parking_lot:
            print(errors.PARKING_LOT_DOES_NOT_EXISTS)
            return

        if command == PARK:
            try:
                registration_number = query_params[1]
                color = query_params[2]
            except Exception as e:
                raise Exception('Missing Registration number or Colour')

            print(parking_lot_helper.park_car(registration_number=registration_number, color=color))
        elif command == LEAVE:
            try:
                slot_number = int(query_params[1])
            except IndexError:
                raise Exception('Missing Slot number')
            except ValueError:
                raise Exception('Slot number should be integer')

            print(parking_lot_helper.vacate_slot(slot_number=slot_number))
        elif command == PARKING_LOT_STATUS:
            print(parking_lot_helper.parking_lot_status())
        elif command == SLOT_NUMBERS_OF_CARS_WITH_COLOR:
            try:
                color = query_params[1]
            except Exception as e:
                raise Exception('Color not Found')

            print(parking_lot_helper.slots_numbers_for_cars_with_color(color=color))
        elif command == REGISTRATION_NUMBERS_OF_CARS_WITH_COLOR:
            try:
                color = query_params[1]
            except Exception as e:
                raise Exception('Color not Found')

            print(parking_lot_helper.registration_numbers_for_cars_with_color(color=color))
        elif command == SLOT_NUMBERS_OF_CARS_WITH_REGISTRATION:
            try:
                registration_number = query_params[1]
            except Exception as e:
                raise Exception('Registration number not Found')

            print(parking_lot_helper.slots_number_of_cars_with_registration_number(
                registration_number=registration_number))
        else:
            print(errors.INVALID_COMMAND)


def read_query():
    try:
        query = input()
        while query != 'exit':
            try:
                run_query(query)
            except Exception as e:
                print(e)

            query = input()

    except Exception as e:
        print(e)


def read_inputfile(file):
    try:
        with open(file) as file:
            queries = file.readlines()
            for query in queries:
                try:
                    run_query(query)
                except Exception as e:
                    print(e)

    except Exception as e:
        print(e)


def main():
    if len(sys.argv) > 1:
        read_inputfile(sys.argv[1])
    else:
        read_query()


if __name__ == '__main__':
    main()
