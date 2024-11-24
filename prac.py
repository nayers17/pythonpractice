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

# iterating through a list 
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"I love {fruit}")

# countdown example
count = 5
while count > 0:
    print(f"counting down: {count}")
    count -= 1
print(f"blast off!")

count = 8
while count > 3:
    print(f"monkey takes one banana and the last number is the amount of monkeys that went without a banana: {count}")
    count -= 1
print(f"3 monkeys did not get banana :(")

# conditionasl: let you execute code only if a specifc requirement is met

# if else example

temperature = 90

if temperature > 85: 
    print("it's hot out here!")

elif temperature < 65:
    print ("brrrrr so cold!")

else:
    print(f"omg feel so good")


# write some data to a file

with open("example.txt", "w") as file:
    file.write("hello, python practice!!!\n")
    file.write("This is line 2.\n")

with open("exampleton.txt", "w") as file:
    file.write("wasssup\n")
    file.write("crackalacka")

with open("yehayehacha.txt", "w") as file:
    file.write("yeha\n")
    file.write("yeha\n")
    file.write("yehacha\n")

with open("yehayehacha.txt", "r") as file:
    content = file.read()
    print(content)

with open("yehayehacha.txt", "a") as file:
    file.write("GREEN EGGS N HAAAAAAAAAAAAAAAM!!!!!!!!\n")
    file.write("PEANUT BUTTER N JAAAAAAAAAAAAAM!!!!!!!!!!!\n")

with open("yehayehacha.txt", "r") as file:
    content = file.read()
    print(content)

# write numbers to a file


with open("numbers.txt", "w") as file:
    for i in range (1, 11):
        file.write(f"{i}\n")

# read and heck in tfunmerbs even or odd

with open("numbers.txt", "r") as file:
    for line in file:
        number = int(line.strip())
        if number % 2 == 0:
            print(f"{number} is even")
        else: 
            print(f"{number} is odd")

