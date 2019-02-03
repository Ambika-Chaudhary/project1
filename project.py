reg_users=[]
global score
score=0
name=input("enter the name")
while name.isalpha() == False:

        print("invalid")
        name = input("enter the name")
        reg_users.append(name)


age = input("enter age")
while age.isnumeric()==False:

        print("invalid age")
        age =input("enter age")
        reg_users.append(age)

password=int(input("enter password to play game"))
while True:
    if password==123456:
        print("valid password")
        reg_users.append(name)
        break
    else:
        print("invalid password")


def menu():
    global score
    print("enter option")
    print("MENU \n 1.USer info \n 2.play game \n 3.quit")
    choice=input()
    if choice=="1":
        print("The registered users are:")
        for x in reg_users:
            print(x)
        menu()
    if choice=="2":
        print("playgame")
        import random
        print("Winning Rules of the Rock paper scissor game as follows: \n"
              + "Rock vs paper->paper wins \n"
              + "Rock vs scissor->Rock wins \n"
              + "paper vs scissor->scissor wins \n")

        while True:
            print("Enter choice \n 1. Rock \n 2. paper \n 3. scissor \n")
            choice = int(input("User turn: "))

            while choice > 3 or choice < 1:
                choice = int(input("enter valid input: "))

            if choice == 1:
                choice_name = 'Rock'
            elif choice == 2:
                choice_name = 'paper'
            else:
                choice_name = 'scissor'

            print("user choice is: " + choice_name)
            print("\nNow its computer turn.......")

            comp_choice = random.randint(1, 3)
            while comp_choice == choice:
                comp_choice = random.randint(1, 3)
            if comp_choice == 1:
                comp_choice_name = 'Rock'
            elif comp_choice == 2:
                comp_choice_name = 'paper'
            else:
                comp_choice_name = 'scissor'

            print("Computer choice is: " + comp_choice_name)

            print(choice_name + " V/s " + comp_choice_name)

            if ((choice == 1 and comp_choice == 2) or
                    (choice == 2 and comp_choice == 1)):
                print("paper wins => ", end="")
                result = "paper"

            elif ((choice == 1 and comp_choice == 3) or
                  (choice == 3 and comp_choice == 1)):
                print("Rock wins =>", end="")
                result = "Rock"
            else:
                print("scissor wins =>", end="")
                result = "scissor"
            if result == choice_name:

                print("<== User wins ==>")
                score=score+1
            else:
                print("<== Computer wins ==>")

            print("Do you want to play again? (Y/N)")
            ans = input()
            if ans == 'n' or ans == 'N':
                #global score
                print("\nThanks for playing")
                print("your Final Score is ",score)

                menu()

    if choice=="3":
        print(quit)

menu()
