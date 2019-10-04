# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

class GroundVehicle():
    def __init__(self, num_wheels = 4): # Set wheels to 4
        self.num_wheels = num_wheels

    # TODO # Create a drive method, have it return "vroooom"
    def drive(self):
        return "vroooom"


# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"

# TODO 
# Create a Motorcycle subclass
# Set num_wheels to 2
# create a new drive method, have it return "BRAAAP!!"

class Motorcycle(GroundVehicle):
    def __init__(self, num_wheels = 2):
        self.num_wheels = num_wheels

    def drive(self):
        return "BRAAAP!!"

vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# Go through the vehicles list and print the result of calling drive() on each.

# TODO
# Loop through the list of vehicles
# Call drive on each as it loops

for i in vehicles:
    i.drive()
