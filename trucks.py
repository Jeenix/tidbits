def main():
    class Vehicle(object):
        """docstring"""

        def __init__(self, color, doors, tires, vtype, cylinder, maxspeed):
            """Constructor"""
            self.color = color
            self.doors = doors
            self.tires = tires
            self.vtype = vtype
            self.cylinder = cylinder
            self.maxspeed = maxspeed

        def brake(self):
            """
            Stop the car
            """
            return "%s braking  with %s doors and %s tires" % (self.vtype, self.doors, self.tires)

        def drive(self):
            """
            Drive the car
            """
            return "I'm driving a %s %s!" % (self.color, self.vtype)

        def coolfactor(self):
            """
            The stuff that makes your car sound cool
            """
            return "My %s %s has a %s engine and max speed of %s km/hr" % (self.color, self.vtype, self.cylinder, self.maxspeed)

    if __name__ == "__main__":
        car = Vehicle("blue", 5, 4, "car", "V8", 240)
        print(car.brake())
        print(car.drive())
        print(car.coolfactor())
        print

        truck = Vehicle("red", 3, 6, "truck", "V6", 120)
        print(truck.drive())
        print(truck.brake())
        print(truck.coolfactor())

if __name__ == '__main__':
    main()