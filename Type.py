#The function type() returns the type of the data it receives as an argument.

print(type('♠'))
print(type(3.1416))
print(type(100))
print(type(1000000000000000000000000000000))
print(type(True))

def OnlyNumbers(arg):
    if type(arg) == int or type(arg) == float:
        print(abs(arg))
    else:
        print("Not a number")


OnlyNumbers(-2.71)