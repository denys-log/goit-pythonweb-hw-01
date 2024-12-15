from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass


class Car(Vehicle):
    def __init__(self, make, model, spec):
        self.make = make
        self.model = model
        self.spec = spec

    def start_engine(self):
        print(f"{self.make} {self.model} ({self.spec} Spec): Двигун запущено")


class Motorcycle(Vehicle):
    def __init__(self, make, model, spec):
        self.make = make
        self.model = model
        self.spec = spec

    def start_engine(self):
        print(f"{self.make} {self.model} ({self.spec} Spec): Мотор заведено")


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make, model):
        pass

    @abstractmethod
    def create_motorcycle(self, make, model):
        pass


class USVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model, "US")

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, "US")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model, "EU")

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, "EU")


if __name__ == "__main__":
    us_factory = USVehicleFactory()
    eu_factory = EUVehicleFactory()

    us_car = us_factory.create_car("Ford", "Mustang")
    us_motorcycle = us_factory.create_motorcycle("Harley-Davidson", "Sportster")

    eu_car = eu_factory.create_car("Volkswagen", "Golf")
    eu_motorcycle = eu_factory.create_motorcycle("Volkswagen", "SP")

    us_car.start_engine()
    us_motorcycle.start_engine()
    eu_car.start_engine()
    eu_motorcycle.start_engine()
