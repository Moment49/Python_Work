import pizza

pizza.make_pizza(16, 'pepperoni', 'mushroom', 'green peppers', 'extra cheese')

# Importing Specific Functions
from pizza import make_pizza

make_pizza(18, 'mozerralla')

# Using as to Give a function an Alias
from pizza import make_pizza as mp

mp(20, 'pepperoni')

# Using as to Give a module an Alias
import pizza as p

p.make_pizza(22, 'pepperoni')

# Importing All functions in a module
from pizza import *

make_pizza(30, 'pepperoni')