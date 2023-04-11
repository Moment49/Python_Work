class User:
    """A class to model a website user"""
    def __init__(self, first_name, last_name, age):
        """A model for a user"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0
       
    def describe_user(self, **user_info):
        """Describe the user"""
        self.user_info = user_info
        user_info['first_name'] = self.first_name 
        user_info['last_name'] = self.last_name 
        user_info['age'] = self.age
        return user_info
    
    def greet_user(self):
        """Greet the user"""
        fullname = f"{self.first_name} {self.last_name}"
        print(f"Welcome to Python, {fullname}")

    def increment_login_attempts(self):
        """Increment the login attempts"""
        self.login_attempts += 1
        print(self.login_attempts)

    def reset_login_attempt(self):
        """Reset the login attempt"""
        if self.login_attempts > 0:
            self.login_attempts = 0
            print(self.login_attempts)





# print(f"Login attempts: {model_user.login_attempts}")
# model_user.reset_login_attempt()
# print(f"Login attempts: {model_user.login_attempts}")

# model_user_dict = model_user.describe_user()
# model_user_dict2 = model_user2.describe_user()
# model_user_dict3 = model_user3.describe_user()
# # Print out user Information
# for key, value in model_user_dict.items():
#     print(f"{key} : {value}")
# print(model_user_dict)
# print(model_user_dict2)
# print(model_user_dict3)
# # Call the greet_user method(To greet user)
# model_user.greet_user()
# model_user2.greet_user()
# model_user3.greet_user()