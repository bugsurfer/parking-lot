import sys

from services.parking_lot_helper import ParkingLotHelper
from constants.errors import errors

parking_lot = None
parking_lot_helper = ParkingLotHelper()


def run_query(query):
    query_params = query.split()
    if query_params[0] == 'create_parking_lot':
        size = query_params[1]
        global parking_lot
        parking_lot = parking_lot_helper.create_parking_lot(size=int(size))
    else:
        if not parking_lot:
            print(errors.PARKING_LOT_DOES_NOT_EXISTS)

        if query_params[0] == 'park':
            registration_number = query_params[1]
            color = query_params[2]
            parking_lot_helper.park_car(registration_number=registration_number, color=color)
        elif query_params[0] == 'leave':
            slot_number = int(query_params[1])
            parking_lot_helper.vacate_slot(slot_number=slot_number)
        elif query_params[0] == 'status':
            parking_lot_helper.parking_lot_status()
        elif query_params[0] == 'slot_numbers_for_cars_with_colour':
            color = query_params[1]
            parking_lot_helper.slots_numbers_for_cars_with_color(color=color)
        elif query_params[0] == 'registration_numbers_for_cars_with_colour':
            color = query_params[1]
            parking_lot_helper.registration_numbers_for_cars_with_color(color=color)
        elif query_params[0] == 'slot_number_for_registration_number':
            registration_number = query_params[1]
            parking_lot_helper.slots_number_of_cars_with_registration_number(registration_number=registration_number)
        else:
            print('Invalid Command')


def read_query():
    try:
        query = input()
        while query != 'exit':
            run_query(query)
            query = input()

    except Exception as e:
        print(e)


def read_inputfile(file):
    try:
        with open(file) as file:
            queries = file.readlines()
            for query in queries:
                run_query(query)
    except Exception as e:
        print(e)


def main():
    if len(sys.argv) > 1:
        read_inputfile(sys.argv[1])
    else:
        read_query()


if __name__ == '__main__':
    main()
