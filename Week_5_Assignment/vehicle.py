class Vehicle:
    def move(self):
        pass  # Subclasses must implement this method

class Car(Vehicle):
    def move(self):
        print("Driving")

class Plane(Vehicle):
    def move(self):
        print("Flying")

class Boat(Vehicle):
    def move(self):
        print("Sailing")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling")

# Example usage
if __name__ == "__main__":
    # Create a list of vehicles
    vehicles = [Car(), Plane(), Boat(), Bicycle()]

    # Iterate through the list and call the move() method for each vehicle
    for vehicle in vehicles:
        vehicle.move()