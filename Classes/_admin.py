from user_mod import User
from admin import *

model_user = User('Elvis', 'Ibenacho', age=26)
model_user2 = User('Tosin', 'Babatunde', age=27)
model_user3 = User('Cassy', 'Temi', age=30)
model_user.increment_login_attempts()

admin_user = User('Elvis', 'Ibenacho', age=26)
admin_user = Admin('Elvis', 'Ibenacho', 27)
admin_user.privileges.show_privileges()
print(admin_user.describe_user())

admin_user_1 = Admin("Kelvin", 'Martin', 24)
admin_user_1.privileges.show_privileges()
print(admin_user_1.describe_user())
