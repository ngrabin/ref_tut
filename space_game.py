"""
Space Travel Game

A simple text adventure written for a refactoring tutorial.
"""

from text_en import TEXT

credits, engines, copilot, game_end = range(4)

def display_inventory(flags):
    print("-" * 79)
    inventory = "\nYou have: "
    inventory += "plenty of credits, " if credits in flags else ""
    inventory += "a hyperdrive, " if engines in flags else ""
    inventory += "a skilled copilot, " if copilot in flags else ""
    if inventory.endswith(", "):
        print(inventory.strip(", "))

def select_planet(destinations):
    """
    Prompt the user to choose a destination from a list of options.
    """
    print("\nWhere do you want to travel?")
    position = 1
    for position, d in enumerate(destinations, 1):
        print(f"[{position}] {d}")

    choice = input()
    return destinations[int(choice) - 1]

 
def visit_planet(planet, flags):
    """interaction with planets"""
    if planet == "earth":
        destinations = ["centauri", "sirius"]
        print(TEXT["EARTH_DESCRIPTION"])

    if planet == "centauri":
        print(TEXT["CENTAURI_DESCRIPTION"])
        destinations = ["earth", "orion"]

        if engines not in flags:
            print(TEXT["HYPERDRIVE_SHOPPING_QUESTION"])
            if input() == "yes":
                if credits in flags:
                    flags.add(engines)
                else:
                    print(TEXT["HYPERDRIVE_TOO_EXPENSIVE"])

    if planet == "sirius":
        print(TEXT["SIRIUS_DESCRIPTION"])
        destinations = ["orion", "earth", "black_hole"]
        if credits not in flags:
            print(TEXT["SIRIUS_QUIZ_QUESTION"])
            answer = input()
            if answer == "2":
                print(TEXT["SIRIUS_QUIZ_CORRECT"])
                flags.add(credits)
            else:
                print(TEXT["SIRIUS_QUIZ_INCORRECT"])

    if planet == "orion":
        destinations = ["centauri", "sirius"]
        if copilot not in flags:
            print(TEXT["ORION_DESCRIPTION"])
            print(TEXT["ORION_HIRE_COPILOT_QUESTION"])
            if input() == "42":
                print(TEXT["COPILOT_QUESTION_CORRECT"])
                flags.add(copilot)
            else:
                print(TEXT["COPILOT_QUESTION_INCORRECT"])
        else:
            print(TEXT["ORION_DESCRIPTION"])

    if planet == "black_hole":
        print(TEXT["BLACK_HOLE_DESCRIPTION"])
        destinations = ["sirius"]
        if input() == "yes":
            if engines in flags and copilot in flags    :
                print(TEXT["BLACK_HOLE_COPILOT_SAVES_YOU"])
                flags.add(game_end)
            else:
                print(TEXT["BLACK_HOLE_CRUNCHED"])
                flags.add(game_end)

    return destinations

def travel():
    print(TEXT["OPENING_MESSAGE"])

    planet = "earth"
    flags = set()
      


    while game_end not in flags:
        
        display_inventory(flags)
        destinations = visit_planet(planet, flags)

        if game_end not in flags:
            planet = select_planet(destinations)

    print(TEXT["END_CREDITS"])


if __name__ == "__main__":
    travel()
