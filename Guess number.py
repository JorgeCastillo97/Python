from random import randint

attempts=int(input("How many chances would you like to have?: "))
number_range= int(input("How many numbers will be?: "))
rnd=randint(1,number_range)
while attempts>0:
    guess=int(input("Try to guess the number: "))
    if rnd==guess:
        print("You won!")
        break;
    attempts-=1
    print("Attempts left:", attempts)

else:
    print("The number was "+str(rnd)+"\nYou're out of attempts.\nYou lost")


input("Press any key to continue...")