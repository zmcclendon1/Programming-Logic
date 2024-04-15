# CONSTANTS
allowedVehicleList = [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan' ]

while True:
    print("****************\n AUTOCARFINDER \n *******************")
    print("\n1. PRINT LIST OF AVAILABLE CARS\nor\n")
    print("2. SEARCH FOR VEHICLE\n")
    print("3. ADD AUTHORIZED VEHICLE\n")
    print("4. EXIT")

    menuInput = input("Enter 1, 2, 3, or 4: ")

    if int(menuInput) == 4:
        print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
        break

    if int(menuInput) == 1:
        print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
        for element in allowedVehicleList:
            print(element)
    if int(menuInput) == 2:
        vehicleInput = input("Enter Vehicle: ")
        isValid = False 
        for vehicle in allowedVehicleList:
            if vehicleInput == vehicle:
                print(f"{vehicleInput} is a valid vehicle")
                isValid = True 
                break 
        if not isValid: 
            print(f"{vehicleInput} is not an authorized vehicle, if you received this in error please check the spelling and try again")
    if int(menuInput) == 3:
        newVehicle = input("Please Enter the full Vehicle name you would like to add: ")
        allowedVehicleList.append(newVehicle)
        print(f"You have added {newVehicle} as an authorized vehicle")
      

