import random as r 

class firstProject:

    def __init__(self):
        self.num_generator = r.randint(0, 20)

    def check(self, B):
        if(self.num_generator == B):
            print("correct!")
        elif(self.num_generator < B):
            print("that's too high")
            print("Here is the correct number: " + str(self.num_generator))
        elif(self.num_generator > B):
            print("that's too low")
            print("Here is the correct number: " + str(self.num_generator))



obj = firstProject()

user = input("Enter a number from 0 to and including 20: \n")

while isinstance(user, str) or user > 20:
    user = input("Please enter a number from 0 to and including 20: \n")

obj.check(user)
