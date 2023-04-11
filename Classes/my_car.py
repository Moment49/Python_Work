import car

my_new_car = car.Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_telsa = car.ElecricCar('tesla', 'model W', 2014)        
print(my_telsa.get_descriptive_name())
