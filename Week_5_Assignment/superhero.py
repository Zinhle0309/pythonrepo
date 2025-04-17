# Base class for a generic superhero
class Superhero:
    def __init__(self, name, alias, superpower, strength_level):
        """Initialize the superhero with unique attributes."""
        self.name = name  # Real name of the superhero
        self.alias = alias  # Superhero alias
        self.superpower = superpower  # Superpower of the superhero
        self.strength_level = strength_level  # Strength level (e.g., on a scale of 1-10)

    def introduce(self):
        """Introduce the superhero."""
        return f"I am {self.alias}, also known as {self.name}. My superpower is {self.superpower}!"

    def use_power(self):
        """Simulate using the superhero's power."""
        return f"{self.alias} uses {self.superpower}!"

    def show_strength(self):
        """Display the superhero's strength level."""
        return f"{self.alias} has a strength level of {self.strength_level}."


# Subclass for superheroes with the ability to fly
class FlyingSuperhero(Superhero):
    def __init__(self, name, alias, superpower, strength_level, flight_speed):
        """Initialize the flying superhero with additional attributes."""
        super().__init__(name, alias, superpower, strength_level)  # Initialize attributes from the base class
        self.flight_speed = flight_speed  # Additional attribute for flight speed

    def fly(self):
        """Simulate flying."""
        return f"{self.alias} is flying at a hypersonic speed of {self.flight_speed} km/h!"

    # Polymorphism: Override the use_power method to provide a unique implementation for flying superheroes
    def use_power(self):
        return f"{self.alias} soars through the sky using a Modular + stealth/space capabilities with a {self.superpower}!"


# Example usage of the classes
if __name__ == "__main__":
    # Create an instance of the base Superhero class
    hero1 = Superhero("Dr Stephen Strange", "Doctor Strange", "Magic, time manipulation, portals, astral projection", 8)
    print(hero1.introduce())  
    print(hero1.use_power())  
    print(hero1.show_strength())  

    # Create an instance of the FlyingSuperhero subclass
    hero2 = FlyingSuperhero("Tony Stark", "Iron Man", "High-Tech Gadgets, Genius intellect, powered suit, flight, weapons", 7, 12200)
    print(hero2.introduce()) 
    print(hero2.use_power())  
    print(hero2.fly())  
