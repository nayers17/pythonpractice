# Variables are used to store data types
name = "Nathan" # string
age = 25 # inte
height = 5.9 # float
is_student = True #boolean
# tuple
# sets
# dictionaries

print(f"My name is {name}. I am {age} years old. I am {height} tall and it is {is_student} I am a student.")

# define a function
def greet(name):
    return f"Hello, {name}!"

# call a function
print(greet("Nathan"))

# more practice

def welcome(name):
    return f"wassup, {name}"

print(welcome("Nathan"))

# more function practice

def scoreboard(score):
    return f"the score is {score}"

print(scoreboard("3 to 2 - Bluejays up one vs. the White Sox"))

# alright one more function

def prerequisite(course):
    return f"You must take {course} to get into Statistics"

print(prerequisite("Linear Alebra"))

# random

print("excellent")

print('onward!@')

# okay now it is time for classes and methods (I knew it)
# classes are a blueprint and outline for creating objects, which is a way to group relative data

# an object is an instance of a class

# defining a class

class Person:
    def __init__(self, name, age): #constructor
        self.name = name
        self.age = age

    def introduce(self): # method
        return f"Hi I am {self.name} and I am {self.age} years old."

# creates an object

person = Person("Nathan", 25)
print(person.introduce())

# seperate 

class scenario:
    def __init__(self, restaurant, time):
        self.restaurant = restaurant
        self.time = time
    
    def example(self):
        return f"I am eating at {self.restaurant} later on in the night towards {self.time}"
    
Scenario = scenario("linguinis yuum", 5)
print(Scenario.example())

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def __str__(self):
        return f"the dogs name is {self.name} and he is a {self.breed}"

dog = Dog("Harlow the Pooch", "cocker spanuil")
print(dog)

    

