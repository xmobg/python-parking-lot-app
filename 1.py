def create_parking_lot(capacity):
    return {
        "capacity": capacity,
        "cars": []
    }


def car_exists(lot, plate):
    for car in lot["cars"]:
        if car["plate"] == plate:
            return True
    return False


def add_car(lot, plate, owner, hours):
    if len(lot["cars"]) >= lot["capacity"]:
        return False

    if car_exists(lot, plate):
        return False

    lot["cars"].append({
        "plate": plate,
        "owner": owner,
        "hours": hours
    })
    return True


def remove_car(lot, plate):
    for car in lot["cars"]:
        if car["plate"] == plate:
            lot["cars"].remove(car)
            return True
    return False


def count_cars(lot):
    return len(lot["cars"])


def cars_over_hours(lot, min_hours):
    return list(filter(lambda car: car["hours"] > min_hours, lot["cars"]))


def total_hours(lot):
    total = 0
    for car in lot["cars"]:
        total += car["hours"]
    return total


def get_plates(lot):
    return list(map(lambda car: car["plate"], lot["cars"]))


def show_all_cars(lot):
    if not lot["cars"]:
        print("Parking is empty")
        return

    for car in lot["cars"]:
        print(f"{car['plate']} - {car['owner']} - {car['hours']}h")



capacity = int(input("Enter parking lot capacity: "))
lot = create_parking_lot(capacity)

while True:
    print("""
1. Add car
2. Remove car
3. Show all cars
4. Show plates only
5. Cars parked over X hours
6. Total hours
7. Current occupancy
0. Exit
""")

    command = int(input("Choose option: "))

    if command == 1:
        plate = input("Plate: ")
        owner = input("Owner: ")
        hours = int(input("Hours parked: "))

        if add_car(lot, plate, owner, hours):
            print("Car added!")
        else:
            print("Cannot add car (duplicate or full)")

    elif command == 2:
        plate = input("Plate to remove: ")

        if remove_car(lot, plate):
            print("Car removed!")
        else:
            print("Car not found")

    elif command == 3:
        show_all_cars(lot)

    elif command == 4:
        plates = get_plates(lot)
        if plates:
            print("Plates:", plates)
        else:
            print("Parking is empty")

    elif command == 5:
        min_hours = int(input("Minimum hours: "))
        result = cars_over_hours(lot, min_hours)

        if result:
            for car in result:
                print(f"{car['plate']} - {car['owner']} - {car['hours']}h")
        else:
            print("No cars parked over that time")

    elif command == 6:
        print("Total hours:", total_hours(lot))

    elif command == 7:
        print(f"{count_cars(lot)}/{lot['capacity']}")

    elif command == 0:
        print("Goodbye!")
        break

    else:
        print("Invalid option")