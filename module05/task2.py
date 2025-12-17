class Car:
    def _init_(self, max_speed):
        self.maximum_speed = max_speed
        self.current_speed = 0
    def accelerate(self, change):
        self.current_speed += change
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        if self.current_speed < 0:
            self.current_speed = 0
car = Car(142)
max_speed = int(input("Enter maximum speed: "))
n = int(input("How many speed changes? "))
for i in range(n):
    change = int(input(f"Enter speed change #{i+1}: "))
    car.accelerate(change)
    print("Current speed:", car.current_speed)
print("Final speed:", car.current_speed)
