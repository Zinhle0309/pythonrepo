from pet import Pet

# Create a pet object
my_pet = Pet(name="Buddy")

# Display initial status
print("Initial Status:")
my_pet.get_status()

# Test the eat method
print("\nAfter eating:")
my_pet.eat()
my_pet.get_status()

# Test the sleep method
print("\nAfter sleeping:")
my_pet.sleep()
my_pet.get_status()

# Test the play method
print("\nAfter playing:")
my_pet.play()
my_pet.get_status()

# Teach the pet some tricks
print("\nTeaching tricks:")
my_pet.train("Sit")
my_pet.train("Roll over")

# Show learned tricks
print("\nLearned Tricks:")
my_pet.show_tricks()