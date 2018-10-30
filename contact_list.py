#!/usr/bin/env python3

"""
Manage contacts

class - Person
Instance Variables  - Name
                    - Phone
                    - email
Methods / functions - methods will be interactiong with instance variable s
    #- access methods (getters)
        - getname()
        - getphone()
        - getemail()
        # what if we want to edit in the future
        mutaters - because they edit the data - setters 
        - setemail()
        - setphone()

"""
"""
# with out object oriented 
#defining main method 
def main():
    
    print("Contact Manager")
    contacts = []
    for i in range(2):
        name = input("enter name ")
        phone = input("enter phone")
        email = input("enter email" )
        contacts.append([name, email, phone])

    for i in range(len(contacts)):
        print("Contact Info")
        for j in range(len(contacts[i])):
            print(contacts[i][j])


                  

# calling the main method
#actual print things or execution starts here 
if __name__ == "__main__":
    main()
    
"""
class Person(object):
    # set up - contructor
        # how you do things or create object out of it
        # self - (instance of the object)object it self 


    def __init__(self, theName, thePhone, theEmail):
        # for particular object
        self.name = theName
        self.phone = thePhone
        self.email = theEmail
    

    # accesser methods - getters
    def getName(self):
        return self.name

    def getPhone(self):
        return self.phone

    def getEmail(self):
        return self.email
    

    # Mutator methods - setters
    def setPhone(self, newPhoneNumber):
        self.phone = newPhoneNumber
    def setEmail(self, newEmail):
        self.email = newEmail

    def __str__(self):
        #override the object -
        return "Person[name = " + self.name + \
               ",phone = " + self.phone + \
               ",email = " + self.email + \
               "]"

def enter_a_friend():
    name = input("enter a friend's name:")
    phone = input("Enter phone number :")
    email = input("Enter email address : ")
    return Person(name, email, phone)

def lookup_a_freind(friends):
    found = False
    name = input("enter a name to lookup:")
    for friend in friends:
        if name in friedn.getName():
            print(friend)
            found = True
    if not found:
        print("No friends match that term : ")

def show_all_friends(friends):
    print("Showing all contacts:")
    for friend in friends:
        print(friend)

def main():
    friends = []
    running = True
    while running:
        print("\n contacts manager")
        print("1) new contact 2) lookup")
        print("3) show all 4) end")
        option = input(">")
        if option == "1":
            friends.append(enter_a_friend())

        elif option == "2":
            lookup_a_friend(friends)
        elif option == "3":
            show_all_friends(friends)
        elif option == "4":
            running = False

        else:
            print("Try Again")
    print("Program is ending")

           
        
"""
def main():
    friend1 = Person("a", '1234', "a@gmail.com")
    print(friend1.getEmail())
    friend1.setEmail("ab@gmail.com")
    print(friend1.getEmail())
    print(friend1)
"""
if __name__ == "__main__":
    main()























