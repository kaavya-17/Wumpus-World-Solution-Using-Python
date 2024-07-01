import random

class WumpusWorld:
    def __init__(self):
        self.size = 4
        self.agent_location = (1, 1)
        self.gold_location = (3, 2)
        self.wumpus_location = (3, 1)
        self.pit_locations = {(1, 3), (2, 4), (3, 3), (4, 4)}
        self.breeze_locations = {(1, 2), (1, 4), (2, 3), (3, 4), (4, 3)}
        self.stench_locations = {(2, 1), (4, 1)}
        self.actions = []

    def move_agent(self, direction):
        x, y = self.agent_location
        if direction == 'up' and x > 1:
            self.agent_location = (x - 1, y)
        elif direction == 'down' and x < self.size:
            self.agent_location = (x + 1, y)
        elif direction == 'left' and y > 1:
            self.agent_location = (x, y - 1)
        elif direction == 'right' and y < self.size:
            self.agent_location = (x, y + 1)
        self.actions.append(f"Moved {direction}")

    def perceive(self):
        x, y = self.agent_location
        perception = ""
        # Check for breeze
        if (x, y) in self.breeze_locations:
            perception += "You feel a breeze!\n"
            # Move to a safe location if breeze is detected
            if 'up' in self.get_valid_actions() and (x - 1, y) not in self.pit_locations:
                self.move_agent('up')
                return "Moved up to a safe location."
            elif 'left' in self.get_valid_actions() and (x, y - 1) not in self.pit_locations:
                self.move_agent('left')
                return "Moved left to a safe location."
            elif 'right' in self.get_valid_actions() and (x, y + 1) not in self.pit_locations:
                self.move_agent('right')
                return "Moved right to a safe location."
        # Check for stench
        elif (x, y) in self.stench_locations:
            perception += "You smell a stench!\n"
        # Check for pit
        if (x, y) in self.pit_locations:
            perception += "Warning: Pit !\n"
            # Move to a safe location if pit is detected
            if 'down' in self.get_valid_actions() and (x + 1, y) not in self.pit_locations:
                self.move_agent('down')
                return "Moved down to a safe location."
            elif 'left' in self.get_valid_actions() and (x, y - 1) not in self.pit_locations:
                self.move_agent('left')
                return "Moved left to a safe location."
            elif 'right' in self.get_valid_actions() and (x, y + 1) not in self.pit_locations:
                self.move_agent('right')
                return "Moved right to a safe location."
        # Check for Wumpus
        if (x, y) == self.wumpus_location:
            perception += "Warning: The Wumpus is nearby!\n"
        # Check for gold
        if (x, y) == self.gold_location:
            perception += "You got the gold and won!\n"
        # If no warnings, indicate safety
        if not perception:
            perception = "You are safe for now.\n"
        return perception

    def get_valid_actions(self):
        x, y = self.agent_location
        valid_actions = []
        if x > 1:
            valid_actions.append('up')
        if x < self.size:
            valid_actions.append('down')
        if y > 1:
            valid_actions.append('left')
        if y < self.size:
            valid_actions.append('right')
        return valid_actions

def reasoning_agent():
    world = WumpusWorld()
    print("Welcome to Wumpus World!")
    while True:
        print("\nYour current perception:")
        perception = world.perceive()
        print(perception)
        if "Pit " in perception or "The Wumpus is nearby" in perception:
            print("Game over!")
            break
        elif "You got the gold" in perception:
            print("Congratulations! You won!")
            break
        else:
            actions = world.get_valid_actions()
            if actions:
                direction = random.choice(actions)
                world.move_agent(direction)
                print(f"Moved {direction} towards the gold_location.")
            else:
                print("No valid actions available. Stuck in the maze!")
                break
reasoning_agent()