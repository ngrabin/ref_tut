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

def engine_puzzle(flags):
    if engines not in flags:
        print(TEXT["HYPERDRIVE_SHOPPING_QUESTION"])
        if input() == "yes":
            if credits in flags:
                flags.add(engines)
            else:
                print(TEXT["HYPERDRIVE_TOO_EXPENSIVE"])

def stellar_quiz(flags):
    if credits not in flags:
        print(TEXT["SIRIUS_QUIZ_QUESTION"])
        answer = input()
        if answer == "2":
            print(TEXT["SIRIUS_QUIZ_CORRECT"])
            flags.add(credits)
        else:
            print(TEXT["SIRIUS_QUIZ_INCORRECT"])

def hire_copilot(flags):
    if copilot not in flags:
        print(TEXT["ORION_HIRE_COPILOT_QUESTION"])
        if input() == "42":
            print(TEXT["COPILOT_QUESTION_CORRECT"])
            flags.add(copilot)
        else:
            print(TEXT["COPILOT_QUESTION_INCORRECT"])

def black_hole(flags):
    if input() == "yes":
        if engines in flags and copilot in flags:
            print(TEXT["BLACK_HOLE_COPILOT_SAVES_YOU"])
            flags.add(game_end)
        else:
            print(TEXT["BLACK_HOLE_CRUNCHED"])
            flags.add(game_end)


STARMAP = {
    "earth": ["centauri", "sirius"],
    "centauri": ["earth", "orion"],
    "sirius": ["orion", "earth", "black_hole"],
    "orion": ["centauri", "sirius"],
    "black_hole": ["sirius"]
}

EVENT_MAP = {
    "centauri": engine_puzzle,
    "sirius": stellar_quiz,
    "orion": hire_copilot,
    "black_hole": black_hole
}

def visit_planet(planet, flags):
    """interaction with planets"""

    key = planet.upper() + '_DESCRIPTION'
    print(TEXT[key])
    EVENT_MAP.get(planet, lambda x:x)(flags)


    return STARMAP[planet]

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
