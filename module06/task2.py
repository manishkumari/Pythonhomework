class Elevator:
    def _init_(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self, elevator = 1):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator {elevator} is now at floor {self.current_floor}")
        else:
            print("Already at the top floor.")

    def floor_down(self, elevator = 1):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator {elevator} is now at floor {self.current_floor}")
        else:
            print("Already at the bottom floor.")

    def go_to_floor(self, target_floor, elevator = 1):
        if target_floor < self.bottom_floor or target_floor > self.top_floor:
            print("Invalid floor.")
            return
        while self.current_floor < target_floor:
            self.floor_up(elevator)
        while self.current_floor > target_floor:
            self.floor_down(elevator)

# elevator = Elevator(1,5)
#
# elevator.floor_up()
# elevator.floor_down()
#
# elevator.go_to_floor(4)

class Building:
    def _init_(self,bottom_floor,top_floor,no_of_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = []

        for i in range(no_of_elevators):
            elevator1 = Elevator(bottom_floor,top_floor)
            self.elevators.append(elevator1)
            print(f"Elevator {i + 1} added.")

    def run_elevators(self, elevator_number, destination_floor):
        if elevator_number < 1 or elevator_number > len(self.elevators):
            print(f"Invalid number of elevators.")
            return

        elevator2 = self.elevators[elevator_number - 1]
        elevator2.go_to_floor(destination_floor, elevator_number)

building = Building(1,10,3)
building.run_elevators(2,5)
building.run_elevators(3,4)
building.run_elevators(2,2)

