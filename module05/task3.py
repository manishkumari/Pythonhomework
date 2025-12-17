class Car:
    def _init_(self):
        self.speed = 0
        self.distance = 0
    def drive(self, hours):
        self.distance = self.distance + self.speed * hours
car = Car()
car.speed = float(input("Enter current speed (km/h): "))
hours = float(input("Enter driving hours: "))
car.distance = float(input("Enter initial travelled distance (km): "))
car.drive(hours)
print(f"Car travelled distance:{car.distance:.2f}km")
