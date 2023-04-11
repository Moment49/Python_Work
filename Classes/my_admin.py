from admin import User
from admin import Privileges
from admin import Admin


admin_user = User('Elvis', 'Ibenacho', age=26)
admin_user = Admin('Elvis', 'Ibenacho', 27)
admin_user.privileges.show_privileges()
print(admin_user.describe_user())

admin_user_1 = Admin("Kelvin", 'Martin', 24)
admin_user_1.privileges.show_privileges()
print(admin_user_1.describe_user())