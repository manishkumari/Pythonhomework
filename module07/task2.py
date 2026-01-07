
class Car:
    def _init_(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change_of_speed):
        self.current_speed += change_of_speed
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        if hours > 0:
            self.travelled_distance += self.current_speed * hours
        else:
            print("Hour should not be negative")

class ElectricCar(Car):
    def _init_(self, registration_number, maximum_speed, battery_capacity):
        super()._init_(registration_number, maximum_speed)
        self.battery_capacity = battery_capacity  # in kWh

class GasolineCar(Car):
    def _init_(self, registration_number, maximum_speed, tank_volume):
        super()._init_(registration_number, maximum_speed)
        self.tank_volume = tank_volume  # in liters


electric_car = ElectricCar("ABC-15", 180, 52.5)
gasoline_car = GasolineCar("ACD-123", 165, 32.3)

electric_car.accelerate(120)
gasoline_car.accelerate(140)

electric_car.drive(3)
gasoline_car.drive(3)

print(f"Electric car ({electric_car.registration_number}) travelled distance: {electric_car.travelled_distance} km")
print(f"Gasoline car ({gasoline_car.registration_number}) travelled distance: {gasoline_car.travelled_distance} km")
