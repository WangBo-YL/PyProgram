'''
Program Name: M03 Lab
Author: Bo Wang
Last Updated: 02/03/2024
Description: A program that allows the user to input car information and display it.
'''
class Vehicle:
    # Constructor
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    # Constructor
    # Inheriting the Vehicle class
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    # Function to display car information
    def display_info(self):
        info = (
            f"Vehicle type: {self.vehicle_type}\n"
            f"Year: {self.year}\n"
            f"Make: {self.make}\n"
            f"Model: {self.model}\n"
            f"Doors: {self.doors}\n"
            f"Roof: {self.roof}\n"
        )
        return info

# Function to collect car information
def collect_car_info():
    print("Please enter the following information about your vehicle:")
    vehicle_type = input("Vehicle type: ")
    year = input("Year: ")
    make = input("Make: ")
    model = input("Model: ")
    doors = input("Doors (2 or 4): ")
    roof = input("Roof (sunroof or hardtop): ")

    car = Automobile(vehicle_type, year, make, model, doors, roof)
    print("\nCar Information:")
    print(car.display_info())


# Main program
# Call the collect_car_info function
collect_car_info()