import unittest


# Определение класса Car
class Car:
    def __init__(self, company, model, year):
        self.company = company
        self.model = model
        self.yearRelease = year
        self.numWheels = 4
        self.speed = 0

    def testDrive(self):
        self.speed = 60

    def park(self):
        self.speed = 0

    def getNumWheels(self):
        return self.numWheels

    def getSpeed(self):
        return self.speed


# Определение класса Motorcycle
class Motorcycle:
    def __init__(self, company, model, year):
        self.company = company
        self.model = model
        self.yearRelease = year
        self.numWheels = 2
        self.speed = 0

    def testDrive(self):
        self.speed = 75

    def park(self):
        self.speed = 0

    def getNumWheels(self):
        return self.numWheels

    def getSpeed(self):
        return self.speed


# Определение тестового класса для проверки функциональности классов Car и Motorcycle
class VehicleTest(unittest.TestCase):

    # Проверка того, что экземпляр объекта Car также является экземпляром транспортного средства
    def test_car_is_vehicle_instance(self):
        car = Car("Toyota", "Corolla", 2022)
        self.assertIsInstance(car, Car)

    # Проверка того, что объект Car создается с 4-мя колесами
    def test_car_has_four_wheels(self):
        car = Car("Toyota", "Corolla", 2022)
        self.assertEqual(car.getNumWheels(), 4)

    # Проверка того, что объект Motorcycle создается с 2-мя колесами
    def test_motorcycle_has_two_wheels(self):
        motorcycle = Motorcycle("Harley-Davidson", "Sportster", 2021)
        self.assertEqual(motorcycle.getNumWheels(), 2)

    # Проверка того, что объект Car развивает скорость 60 в режиме тестового вождения (testDrive())
    def test_car_speed_on_test_drive(self):
        car = Car("Toyota", "Corolla", 2022)
        car.testDrive()
        self.assertEqual(car.getSpeed(), 60)

    # Проверка того, что объект Motorcycle развивает скорость 75 в режиме тестового вождения (testDrive())
    def test_motorcycle_speed_on_test_drive(self):
        motorcycle = Motorcycle("Harley-Davidson", "Sportster", 2021)
        motorcycle.testDrive()
        self.assertEqual(motorcycle.getSpeed(), 75)

    # Проверить, что в режиме парковки машина останавливается (speed = 0)
    def test_car_stops_when_parked(self):
        car = Car("Toyota", "Corolla", 2022)
        car.testDrive()
        car.park()
        self.assertEqual(car.getSpeed(), 0)

    # Проверить, что в режиме парковки мотоцикл останавливается (speed = 0)
    def test_motorcycle_stops_when_parked(self):
        motorcycle = Motorcycle("Harley-Davidson", "Sportster", 2021)
        motorcycle.testDrive()
        motorcycle.park()
        self.assertEqual(motorcycle.getSpeed(), 0)


if __name__ == '__main__':
    unittest.main()
