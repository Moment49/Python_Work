from user_mod import User

class Privileges:
    """An attempt to assign privileges for a super user"""
    def __init__(self, *privileges):
        self.privileges = privileges

    def show_privileges(self):
        """Show list of Admin privileges"""
        print('This is the list of Admin rights: ')
        for privilege in self.privileges:
            print(privilege)

# 9.7 Admin
class Admin(User):
    """Attempt to model an admin user of a website"""
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.privileges = Privileges("can add post", "can delete post", "can ban user")
        
 

