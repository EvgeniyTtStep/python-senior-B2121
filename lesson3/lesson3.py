class Human:
    def __init__(self, name="Human"):
        self.name = name


class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passenger(self, *args):
        for passanger in args:
            self.passengers.append(passanger)

    def print_passengers_names(self):

        if self.passengers != []:
            print(f"Names of {self.brand} passengers: ")
            for passenger in self.passengers:
                print(passenger.name)
        else:
            print(f"There are no passengers in {self.brand}")


# =====================================


nick = Human("Nick")
kate = Human("Kate")
jack = Human("Jack")
car = Auto("Mercedes")

car.add_passenger(nick, kate, jack)


car.print_passengers_names()
