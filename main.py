from time import sleep

class Trail:

    def __init__(
            self,
            name: str,
            distance: float,
            if_completed: bool = False
    ) -> None:
        self.name = name
        self.distance = distance
        self.if_completed = if_completed

    @property
    def status(self) -> str:
        if self.if_completed:
            return "Completed"
        return "Not completed"

    def update (self, **changes) -> None:
        for key, value in changes.items():
            setattr(self, key, value)


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

def show_trails(trails: list[Trail]) -> None:
    for i, trail in enumerate(trails):
        print(f"{i + 1}. {trail.name}, {trail.distance}km, {trail.status}")

def filter_trails(
    trails: list[Trail],
    trail_distance: float
) -> list[Trail]:
    return list(
        filter(
            lambda trail: trail.distance <= trail_distance,
            trails
        )
    )

def mark_as_completed(trails: list[Trail], index: int) -> None:
    trails[index].if_completed = True
    print("Trail status changed to completed!\n")

while True:
    print("\n\n=========================")
    print(" THE TRAIL COMPANION APP")
    print("=========================\n")
    print("Choose a menu option (enter the corresponding number):")
    print("[1] Show all trails")
    print("[2] Find trails by maximum distance")
    print("[3] Mark trail as completed")
    print("[4] Edit trails")
    print("[5] Exit")

    user_menu_option = int(input())

    match user_menu_option:
        case 1:
            print("YOUR TRAILS:")
            show_trails(trails_list)
            sleep(2)
        case 2:
            print(
                "\nPlease input the maximum distance in kilometers and I'll print out the appropriate trails for you:")
            expected_trail_distance = float(input())
            show_trails(filter_trails(trails_list, expected_trail_distance))
            sleep(2)
        case 3:
            show_trails(trails_list)
            print("\nEnter the chosen trail's list number:")
            chosen_trail_number = int(input())
            mark_as_completed(trails_list, chosen_trail_number - 1)
            sleep(2)
        case 4:
            print("YOUR TRAILS:")
            show_trails(trails_list)
            print("\nWhich trail do you want to edit?")
            chosen_trail_number = int(input())

            print("Please insert new data:")
            print("Name:")
            new_name = input()
            print("Distance:")
            new_distance = float(input())

            trails_list[chosen_trail_number - 1].update(name = new_name, distance = new_distance)
            sleep(2)
        case 5:
            print("\nGoodbye!")
            sleep(2)
            exit(0)
        case _:
            print("Invalid option")

