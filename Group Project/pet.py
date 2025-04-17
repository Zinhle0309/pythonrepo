class Pet:
    def __init__(self, name, hunger=5, energy=5, happiness=5):
        """
        Initialize a new pet with a name, hunger, energy, and happiness levels.
        Default values for hunger, energy, and happiness are set to 5.
        """
        self.name = name
        self.hunger = hunger  # Hunger level (0 = full, 10 = very hungry)
        self.energy = energy  # Energy level (0 = tired, 10 = fully rested)
        self.happiness = happiness  # Happiness level (0–10)
        self.tricks = []  # List to store learned tricks

    def eat(self):
        """
        Reduces hunger by 3 points (but not below 0) and increases happiness by 1 (up to 10).
        """
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)

    def sleep(self):
        """
        Increases energy by 5 points (but not above 10).
        """
        self.energy = min(10, self.energy + 5)

    def play(self):
        """
        Decreases energy by 2, increases happiness by 2 (up to 10), 
        and increases hunger by 1 (up to 10). If energy is less than 2, 
        the pet cannot play.
        """
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
        else:
            print(f"{self.name} is too tired to play!")

    def get_status(self):
        """
        Prints the current state of the pet, including its name, hunger, energy, and happiness levels.
        """
        print(f"Name: {self.name}")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")

    def train(self, trick):
        """
        Teaches the pet a new trick and adds it to the list of tricks.
        """
        self.tricks.append(trick)
        print(f"{self.name} has learned a new trick: {trick}!")

    def show_tricks(self):
        """
        Prints all the tricks the pet has learned. If no tricks have been learned, 
        it notifies the user.
        """
        if self.tricks:
            print(f"{self.name} knows the following tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")