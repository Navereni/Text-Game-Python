name = input("Name: ")
age = int(input("Age: "))

health = 10

if age >= 18:
    print("You are old enough")
    lets_play = input("Do you want to play? ")
    if lets_play == "yes":
        print("Let's play. You are starting with", health, "health")
    elif lets_play == "no":
        print("see you later")
elif age >= 14:
    print("you can play with parents")
    lets_play = input("Do you want to play? ")
    if lets_play == "yes":
        print("Let's play. You are starting with", health, "health")
    elif lets_play == "no":
        print("see you later")
else:
    print("You are not old enough")

left_or_righ = input("Do you want to go left or right?(left/right) ").lower()
if left_or_righ == "left":
    ans = input("You arrive to a huge wall. Do you want to look for another way or go back(another/back) ")
    if ans == "another":
        print("Stone fell of the wall and hit you in the heard. You didn't had any protection so You lost 5 health. \nBut You found a door.")
        health -= 5
        print("Your have", health, "health now")
        ans = input("Do You want to open them?(yes/no)? ")
        if ans == "yes":
            print("Looks like the doors haven't been opened for a long time. It took a lot of effort to open them. \nIt's dark inside, but you are desperate to have a nap.")
            ans = input("Do You want to enter and look for a place to sleep or stay outside(yes/no)? ")
        else:
            print("You decide to stay outside. You are tired so You need to look for a place to sleep")
            if ans == "yes":
                print("After a bit of searching You found a switch. After You switched on light You start to look for a bedroom.\nYou found it. planing to go to sleep.")
                ans = input("Do You want to lock the house doors or not(yes/no)? ")
elif left_or_righ == "right":
    print("You arrive to a huge lake.")
    ans = input("Do you want to swim or walk around?(swim/around) ")
    if ans == "swim":
        print("You got to other side")
    else:
        print("go around you fool")
