import logging
from abc import ABC, abstractmethod
from typing import Protocol

# Налаштування логування
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


# Абстрактний клас Vehicle
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self) -> None:
        pass


# Клас Car
class Car(Vehicle):
    def __init__(self, make: str, model: str, spec: str) -> None:
        self.make: str = make
        self.model: str = model
        self.spec: str = spec

    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model} ({self.spec} Spec): Двигун запущено")


# Клас Motorcycle
class Motorcycle(Vehicle):
    def __init__(self, make: str, model: str, spec: str) -> None:
        self.make: str = make
        self.model: str = model
        self.spec: str = spec

    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model} ({self.spec} Spec): Мотор заведено")


# Абстрактна фабрика VehicleFactory
class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Car:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        pass


# Фабрика для США
class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, "US")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, "US")


# Фабрика для ЄС
class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, "EU")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, "EU")


# Основна логіка програми
if __name__ == "__main__":
    us_factory: VehicleFactory = USVehicleFactory()
    eu_factory: VehicleFactory = EUVehicleFactory()

    us_car: Vehicle = us_factory.create_car("Ford", "Mustang")
    us_motorcycle: Vehicle = us_factory.create_motorcycle(
        "Harley-Davidson", "Sportster"
    )

    eu_car: Vehicle = eu_factory.create_car("Volkswagen", "Golf")
    eu_motorcycle: Vehicle = eu_factory.create_motorcycle("Volkswagen", "SP")

    us_car.start_engine()
    us_motorcycle.start_engine()
    eu_car.start_engine()
    eu_motorcycle.start_engine()
