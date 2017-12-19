# Making a basic calculator

"""
Creating
some functions
"""
import math
# from math import *
# from math import sqrt


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mult(a, b):
    return a * b


def div(a, b):
    return a / b


def exp(a, b):
    return a ** b


def sqt(a, b):
    return math.sqrt(add(a, b))


def mod(a, b):
    return a % b


def err():
    print("Type a valid option!")


print("\t\t\tCalculator\n\n")

n1 = input("Type the first number: ")
n2 = input("Type the second number: ")
op = input(
    "Choose an option\n1)Addition\n2)Subtraction\n"\
    "3)Multiplication\n4)Division\n5)Exponentiation\n6)Squared Root\n7)Modulo\n")

n = int(op)

if n == 1:
    print(add(int(n1), int(n2)))
elif n == 2:
    print(sub(int(n1), int(n2)))
elif n == 3:
    print(mult(int(n1), int(n2)))
elif n == 4:
    print(div(int(n1), int(n2)))
elif n == 5:
    print(exp(int(n1), int(n2)))
elif n == 6:
    print(sqt(int(n1), int(n2)))
elif n == 7:
    print(mod(int(n1), int(n2)))
else:
    err()

functions=dir(math)

print("This is math:\n"+str(dir(math)))

input("Press any key to continue...")


