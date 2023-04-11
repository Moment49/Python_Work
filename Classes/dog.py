# OBJECTS
# class Dog:
#     """A simple attempt to model a dog"""
#     def __init__(self, name, age):
#         """Initialize name and age attributes"""
#         self.name = name
#         self.age = age
    
#     def sit(self):
#         """Simulate a dog sitting in response to a command."""
#         print(f"{self.name} is now sitting")
    
#     def roll_over(self):
#         """Simulate rolling over in response to a command"""
#         print(f"{self.name} rolled over!")

# my_dog = Dog('willie', 7)
# print(f"My dog's name is {my_dog.name}")
# print(f"My dog is {my_dog.age} years old")
# # Calling methods
# my_dog.sit()
# my_dog.roll_over()

# # Creating multiple Instances
# your_dog = Dog('Lucy', 3)
# print(f"\nYour dog's name is {your_dog.name}")
# print(f"Your dog is {your_dog.age} years old")
# your_dog.sit()
# your_dog.roll_over()

# Working with Classes and Instances & Setting default value fo an attribute


# my_used_car = Car('toyota', 'outback', 2014)
# print(my_used_car.get_descriptive_name())

# my_used_car.update_odometer(2300)
# my_used_car.read_odometer()

# my_used_car.increment_odometer(500)
# my_used_car.read_odometer()
# Modifying Attributes Values directly
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()

# Inheritance
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """Return neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")

    # Modifying an Attribute's value through a method
    def update_odometer(self, mileage):
        """Set the odometer reading to a given value
            and reject change if it attempts to roll the odometer back 
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading"""
        self.odometer_reading += miles

#Instance as Attributes
class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size = 75):
        """Initialize the battery attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""    
        print(f"This car has a {self.battery_size}-kwh battery.")
    
    def get_range(self):
        """Print a statement about the range this battery provides"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on full charge.")

# Defining Attributes and methods for the child class
class ElecricCar(Car):
    """Represents aspects of a car, specific to electric vehicles"""

    def __init__(self, make, model, year):
        """Initialize attributes of a car specific to electric vehicles"""
        super().__init__(make, model, year)
        self.battery = Battery(100)


my_telsa = ElecricCar('tesla', 'model s', 2023)        
print(my_telsa.get_descriptive_name())
my_telsa.battery.describe_battery()
my_telsa.battery.get_range()


