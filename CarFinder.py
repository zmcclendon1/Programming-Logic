# CONSTANTS
allowedVehicleListFilePath = "AllowedVehicleList.txt"

# Function to read the allowed vehicle list from the file
def read_vehicle_list():
    with open(allowedVehicleListFilePath, "r") as file:
        return file.read().splitlines()

# Function to write the updated vehicle list back to the file
def write_vehicle_list(vehicle_list):
    with open(allowedVehicleListFilePath, "w") as file:
        for vehicle in vehicle_list:
            file.write(vehicle + "\n")

# Main application loop
def main():
    vehicle_list = read_vehicle_list()

    while True:
        print("****************\n AUTOCARFINDER \n *******************")
        print("\n1. PRINT LIST OF AVAILABLE CARS\nor\n")
        print("2. SEARCH FOR VEHICLE\n")
        print("3. ADD AUTHORIZED VEHICLE\n")
        print("4. DELETE AUTHORIZED VEHICLE\n")
        print("5. EXIT")

        menu_input = input("Enter 1, 2, 3, 4, or 5: ")

        if int(menu_input) == 5:
            print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
            break

        if int(menu_input) == 1:
            print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
            for vehicle in vehicle_list:
                print(vehicle)

        if int(menu_input) == 2:
            vehicle_input = input("Enter Vehicle: ")
            if vehicle_input in vehicle_list:
                print(f"{vehicle_input} is a valid vehicle")
            else:
                print(f"{vehicle_input} is not an authorized vehicle, if you received this in error please check the spelling and try again")

        if int(menu_input) == 3:
            new_vehicle = input("Please Enter the full Vehicle name you would like to add: ")
            vehicle_list.append(new_vehicle)
            write_vehicle_list(vehicle_list)
            print(f"You have added {new_vehicle} as an authorized vehicle")

        if int(menu_input) == 4:
            deleted_vehicle = input("Please Enter the full Vehicle name you would like to REMOVE: ")
            confirmation = input(f"Are you sure you want to remove {deleted_vehicle} from the Authorized Vehicles List? (yes/no): ")
            if confirmation.lower() == "yes":
                vehicle_list.remove(deleted_vehicle)
                write_vehicle_list(vehicle_list)
                print(f"You have REMOVED {deleted_vehicle} as an authorized vehicle")
            elif confirmation.lower() == "no":
                print("Thank you")

if __name__ == "__main__":
    main()