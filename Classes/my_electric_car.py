# from car import  Car, ElecricCar
from car import  Car
from electricCar import ElecricCar as EC

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_telsa = EC('tesla', 'model s', 2023)        
print(my_telsa.get_descriptive_name())
my_telsa.battery.describe_battery()
my_telsa.battery.get_range()