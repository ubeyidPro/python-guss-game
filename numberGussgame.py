
from numpy import random

print("#### Number Guss Game ###")


trial = 0
computer_guss = random.randint(10)

while True:
    try:
        user_gess = int(input("what's your guss? \n >>> "))
        if(user_gess == computer_guss):
            print('You win.' , trial ,'times' )
            trial = 0
            
            while True:
                user_per = input("Try agin? (Y/N)  ");
                if(user_per == 'Y' or user_per == "y" or user_per == 'N' or user_per == "n"):
                    break
                else:
                    print("Enter only yes(Y,y) no(N,n)");
            
            if(user_per == 'Y' or user_per == "y"):
                computer_guss = random.randint(10)
            elif (user_per == 'N' or user_per == "n"):
                break
            else:
                print('somting is wrong!')

        elif(user_gess < computer_guss):
            print('too low.')
            trial += 1
        elif(user_gess > computer_guss):
            print('too high.')
            trial += 1
        else:
            print('Please type number btween 1 to 10')
 
    except :
        print('please only numbers')   