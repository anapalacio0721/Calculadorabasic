class User:
    def __init__(self,name,email,password):
        self.name= name
        self.email= email
        self.password= password

    def get_name(self):
        print("My name is " + self.name)

    def get_email(self):
        print("My email is " + self.email)

    def get_email(self):
        print("My password is " + self.password)

    def get_data(self):
        self.get_name()
        self.get_email()

def main():
    user1= User("ana", "ana@hotmail.com", "1234")
    print("information of the user")
    print(user1.name)
    print(user1.email)
    print(user1.password)
    user1.name= "luis"
    print(user1.name)



if __name__ == "__main__":
    main()


