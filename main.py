from time import sleep

class Trail:

    def __init__(self, name, distance, if_completed="Not completed"):
        self.name = name
        self.distance = distance
        self.if_completed = if_completed


# Pine Ridge Loop - 4.8 km
# Silver Lake Trail - 7.2 km
# Mossy Creek Path - 3.5 km
# Eagle Peak Trail - 11.6 km
# Fern Valley Walk - 6.1 km

trail_1 = Trail("Pine Ridge Loop", 4.8)
trail_2 = Trail("Silver Lake Trail", 7.2)
trail_3 = Trail("Mossy Creek Path", 3.5)
trail_4 = Trail("Eagle Peak Trail", 11.6)
trail_5 = Trail("Fern Valley Walk", 6.1)

trails_list = [trail_1, trail_2, trail_3, trail_4, trail_5]

def show_trails(trails):
    for trail in trails:
        print(str(trails.index(trail) + 1) + ". " + trail.name + ", " + str(
            trail.distance) + "km, " + trail.if_completed)

def mark_as_completed(trails, index):
    if trails[index].if_completed == "Not completed":
        trails[index].if_completed = "Completed"
    print("Trail status changed to completed!\n")

while True:
    print("\n\n=========================")
    print(" THE TRAIL COMPANION APP")
    print("=========================\n")
    print("Choose a menu option (enter the corresponding number):")
    print("[1] Show all trails")
    print("[2] Find trails by maximum distance")
    print("[3] Mark trail as completed")
    print("[4] Exit")

    user_menu_option = int(input())

    match user_menu_option:
        case 1:
            print("YOUR TRAILS:")
            show_trails(trails_list)
            sleep(2)
        case 2:
            print(
                "\nPlease input the maximum distance in kilometers and I'll print out the appropriate trails for you:")
            expected_trail_distance = input()

            if expected_trail_distance.isdigit():
                expected_trail_distance = int(expected_trail_distance)

            filtered_trails = filter(
                lambda trail: trail.distance <= expected_trail_distance,
                trails_list
            )
            show_trails(filtered_trails)
            sleep(2)
        case 3:
            show_trails(trails_list)
            print("\nEnter the chosen trail's list number:")
            chosen_trail_number = int(input())

            mark_as_completed(trails_list, chosen_trail_number - 1)
            sleep(2)
        case 4:
            print("\nGoodbye!")
            sleep(2)
            exit(0)
        case _:
            print("Invalid option")

