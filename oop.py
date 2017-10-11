class User(object):
    def __init__(self, name, email, phonenumber):
        self.name = name
        self.email = email
        self.logged = False
        self.phonenumber = phonenumber
    def login(self):
        self.logged = True
        print "{} is logged in.".format(self.name)
        return self

new_user = User("Anna", "anna@anna.com", 3054421010)
print new_user.login()
