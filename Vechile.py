class Vehicle:
    def move(self):
        print("This vehicle moves in a general way.")

class Car(Vehicle):
    def move(self):
        print("Driving on roads 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying through the sky ✈️")

class Bike(Vehicle):
    def move(self):
        print("Riding on two wheels 🚴")

class Boat(Vehicle):
    def move(self):
        print("Sailing across water 🚤")

# Test polymorphism
vehicles = [Car(), Plane(), Bike(), Boat()]

for v in vehicles:
    v.move()
