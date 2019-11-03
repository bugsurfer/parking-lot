# parking_lot
GOJEK Parking Lot Assignment

I have implemented the solution in Python

My Approach for the problem is to created a dictionary (map)
between slot numbers and Slot(Object). Remember a dictionary in python is always sorted so when an slot is available it allocates the one with the least slot number hence nearest

Assumptions:
I am assuming that the same car is not allowed to park agains
I have added a method to check whether the car already parked but it always returns False


I have created 3 classes:
Slot
ParkingLot
Car

I have also included a file file.txt which has sample input

How to Run?
Step 1: Go inside the parking Lot
Step 2: Run bin/setup
        This installs all the dependencies required(Python 3). This may take a while around 3 minutes

        It also runs the TestSuite which contain test classes

Step 3: Executing the application code
        Interactive Way:
          Run bin/parking_lot
          and now Give any of the below commands
          1.create_parking_lot
          2.park
          3.leave
          4.status
          5.slot_numbers_for_cars_with_colour
          6.slot_number_for_registration_number
          7.registration_numbers_for_cars_with_colour

        FileInput Way:
          Run bin/parking_lot parking_lot/file.txt

Running Test Suite
Run python3 parking_lot.py after cd into tests directory

NOTE: you need to cd to tests directory to run the TestSuite


      
