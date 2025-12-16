def gallons_to_liters(gallons):
    return gallons * 3.78541
while True:
    gallons = float(input("Enter gallons: "))
    if gallons < 0:
        print ("Invalid input")
        break
    liters = gallons_to_liters(gallons)
    print(f"{gallons} gallons = {liters:.2f} liters")
def gallons_to_liters(gallons):
    return gallons * 3.78541
while True:
    gallons = float(input("Enter gallons: "))
    if gallons < 0:
        print ("Invalid input")
        break
    liters = gallons_to_liters(gallons)
    print(f"{gallons} gallons = {liters:.2f} liters")
