rooms = {}

for room in ("A", "B"):
    while True:
        state = input(f"Is room {room} dirty or clean? ").strip().lower()
        if state in ("dirty", "clean"):
            rooms[room] = state
            break
        print("Please enter 'dirty' or 'clean'.")


def is_dirty(room):
    """Check whether the given room needs cleaning."""
    return rooms[room] == "dirty"


def clean_room(room):
    """Change a room's state to clean."""
    rooms[room] = "clean"


print("Initial room states:", rooms)

class VacuumAgent:
    def __init__(self, starting_room="A"):
        self.location = starting_room

    def move(self):
        """Switch to the other room."""
        self.location = "B" if self.location == "A" else "A"

    def perceive_and_act(self):
        """Clean a dirty room; otherwise move to the other room."""
        if is_dirty(self.location):
            cleaned_room = self.location
            clean_room(cleaned_room)
            return f"Cleaned room {cleaned_room}"

        previous_room = self.location
        self.move()
        return f"Moved from room {previous_room} to room {self.location}"

agent = VacuumAgent()

while True:
    try:
        num_steps = int(input("How many steps should the simulation run? "))
        if num_steps > 0:
            break
        print("Please enter a number greater than zero.")
    except ValueError:
        print("Please enter a whole number.")

for step in range(1, num_steps + 1):
    starting_location = agent.location
    action = agent.perceive_and_act()

    print(f"Step {step}")
    print(f"  Started in: Room {starting_location}")
    print(f"  Action: {action}")
    print(f"  Ended in: Room {agent.location}")
    print(f"  Room states: {rooms}")


