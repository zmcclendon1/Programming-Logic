# CONSTANTS
ALLOWED_VEHICLE_LIST = [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan' ]


print("****************\n AUTOCARFINDER \n *******************")
print("\n1. PRINT LIST OF AVAILABLE CARS\nor\n")
print("2. SEARCH FOR VEHICLE\n")
print("3. EXIT")

menuInput = input("Enter 1, 2, or 3: ")


if int(menuInput) == 3:
    print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")

if int(menuInput) == 1:
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for element in ALLOWED_VEHICLE_LIST:
        print(element)
if int(menuInput) == 2:
    vehicleInput = input("Enter Vehicle: ")
    isValid = False 
    for vehicle in ALLOWED_VEHICLE_LIST:
        if vehicleInput == vehicle:
            print(f"{vehicleInput} is a valid vehicle")
            isValid = True 
            break 
    if not isValid: 
        print(f"{vehicleInput} is not an authorized vehicle, if you received this in error please check the spelling and try again")