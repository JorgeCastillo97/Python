a = int(input("Type the first number: "))
b = int(input("The second one: "))
c = int(input("The third one: "))
d = int(input("The fourth one: "))
e = int(input("The last one: "))


def biggest(*args):
    print("The biggest is: " + str(max(args)))


def smallest(*args):
    print("The smallest is: " + str(min(args)))


def distance_from_zero(x):
    print("Distance from zero: %d" %abs(x))


# Send the functions as many parameters as you want
biggest(a, b, c, d, e)
smallest(a, b, c, d, e)
distance_from_zero(-(a+b+c+d+e))

input("Press any key to continue...")