class Restaurant:
    """An attempt to model a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the name and cuisine type of the restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 23
    def describe_restaurant(self):
        """Describe the restaurant"""
        print(f"\nThe name of the restaurant is {self.restaurant_name}")
        print(f"The sell a delicious {self.cuisine_type} cuisine")
    def open_restaurant(self):
        """Open the restaurant"""
        print(f"The {self.restaurant_name} is now open")
        print(f"The restaurant has served {self.number_served} customers")

    def set_number_served(self, num_served):
        """Add the number of customers served"""
        if num_served >= self.number_served:
            self.number_served = num_served
        else:
            print('We cant serve again')
    def increment_number_served(self, increment_serves):
        """Increment the number of customers been served"""
        self.number_served += increment_serves

