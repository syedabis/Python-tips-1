def get_price(food: str):
    if food == "apple" or food == "peach":
        return 4
    elif food == "orange":
        return 3
    elif food == "grape":
        return 5
    else:
        return "Unknown"

print(get_price("peach")) # Output: 4

def get_price(food: str):
    match food:
        case "apple" | "peach":
            return 4
        case "orange":
            return 3
        case "grape":
            return 5
        case _:
            return "Unknown"

print(get_price("peach")) # Output: 4
