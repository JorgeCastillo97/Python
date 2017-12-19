from random import randint

count=0

while count<5:
    print("Count is", count)
    count+=1

while True:
    if count>10:
        break
    else:
        print("count:", count)
    count+=1

num=1
while num<=10:
    print(num**2)
    num+=1

"""choice = input("Enter y or n only: ")
while choice!= "y" and choice!="n":
    choice = input("Try again. y or n: ")"""

count=0
while count<3:
    number=randint(1,6)
    print(number)
    if number == 1:
        print("Loop finished")
        break
    else:
        print("You are lucky")
    count+=1

#for loops

print("Counting...")

for i in range(10):
    print(i)
print("\n")

sentence= "Programming in Python!"

for letter in sentence:
    print (letter, end="")

dict = {
    "a": "apple",
    "b": "banana",
    "c": "cheery"
}
print("\n")

for key in dict:
    print("Key: "+str(key)+"\tValue: "+str(dict[key]))

choices=['pizza','burguer','pasta','salad', 'milkshake']
print("\n")

for index, item in enumerate(choices):
    print((index+1), item)

print("\n")

fruits = ['banana', 'apple', 'orange', 'carrot', 'pear', 'grape']

print("You have...")
for f in fruits:
    if f == 'carrot':
        print ('A carrot is not a fruit!')
        break
    print ('A', f)
#the "else" statement is not executed because of the "Break" inside the for loop
else:
    print ('A fine selection of fruits!')