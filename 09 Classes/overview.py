# Class, Objects, Instances, Attributes, Methods
class Dog:
    """A simple attempt to model a dog."""
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")
    def roll_over(self):
        """Simulate rolling over in responseto a command."""
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

'''
Making an object from a class is called instantiation.
my_dog refers to single instance created from a class.
name, age are called attributes. (Basically variables that describe class)
Functions inside a class are called methods.
'''

# Setting a Default Value for an Attribute
class Car:
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0   # default
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

# Modifying an Attribute’s Value Directly
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23            # modifying directly
my_new_car.read_odometer()

# Modifying an Attribute’s Value Through a Method
class Car:
    '''---snip---'''
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        self.odometer_reading = mileage

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)              # update through method


# INHERITANCE
# The __init__() Method for a Child Class
class Car:
    '''---snip---'''
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)         # calls __init__ method of parent class, Car. (superclass)

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())

# Defining Attributes and Methods for the Child Class
class Car:
    '''---snip---'''
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class. Then initialize attributes specific to an electric car."""
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

# Overriding Methods from the Parent Class
'''Say the class Car had a method called fill_gas_tank(). 
This method is meaningless for an all-electric vehicle, so you might want to override this method.'''

class ElectricCar(Car):
    '''--snip--'''
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")   # Program considers only the method in child class instead of method in parent class

# Instances as Attributes
'''if we continue adding detail to the Electric Car class, we might notice that we're adding many attributes and methods 
specific to the car's battery. When we see this happening, we can stop and move those attributes and methods to a separate 
class called Battery. Then we can use a Battery instance as an attribute in the ElectricCar class'''
class Car:
    '''---snip---'''
class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery() # this tells python to look at instance my_telsa, find its battery attribute and call method 
                                    #   descriptive_battery()

# Importing Classes
# Importing a Single Class
'''Storing class Car in car.py and present working file is renamed as my_car.py'''
from car import Car     # importing class Car from module(file) car

# Importing Multiple Classes from a Module
from car import Car, ElectricCar

# Importing an Entire Module
import car

# Importing All Classes from a Module
from module_name import *

# 