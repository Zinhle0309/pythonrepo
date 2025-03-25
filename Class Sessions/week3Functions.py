# Function definition
def greet(name):
    """Greet a person by their name."""
    return f"Hello, {name}!"

# Function call
print(greet("Alice"))  # Output: Hello, Alice!

#Positional Arguments:

def add(a, b):
    return a + b

print(add(3, 5))  # Output: 8 

#Default Arguments:

def greet(name="Guest"):
    return f"Hello, {name}!"

print(greet())  # Output: Hello, Guest!
print(greet("Alice"))  # Output: Hello, Alice!

#Keyword Arguments:

def introduce(name, age):
    return f"My name is {name}, and I'm {age} years old."

print(introduce(age=25, name="Bob"))  # Output: My name is Bob, and  I'm 25 years old.

# Lambda function for adding two numbers
add = lambda x, y: x + y
print(add(3, 5))  # Output: 8

# Using lambda with map()
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, numbers))
print(squares)  # Output: [1, 4, 9, 16]

#A function can call itself, enabling recursive problem-solving.

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120