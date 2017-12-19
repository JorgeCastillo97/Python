names=["Adam","Alex","Mariah","Martin","Spencer"]
for n in names:
    print(n)


print("\n\n")
webster={
    "Cartoon Network" : "A TV Channel for kids.",
    "Blark" : "The sound a dog makes.",
    "Carpet" : "Goes on the floor.",
    "Dab" : "A small amount."
}

for w in webster:
    print(webster[w])


print("\n\n")
a=[1,2,3,4,5,6,7,8,9,10]
for b in a:
    if b%2==0:
        print(b)


print("\n\n")


def redOnes ( subset ):
    count=0
    for color in subset:
        if color=="Red":
            count=count+1

    return count


subset=["Red","Blue","Yellow","Black","White","Red","Gold","Cyan","Red","Orange"]
subset.append("Black")
subset[0]="Red"
print("Colors:\n")
print(subset)
last_3=subset[8:len(subset)]
print("The last three elements are: %s" %last_3)
print("Gold is in position: %d" %subset.index("Gold"))
subset.insert(subset.index("Gold"), "Deleted")
print(subset[6])
print("\nRed ones found:\n%d"%redOnes(subset))


print("\n\n")
for letter in "Programming in Python":
    if letter=="i":
        print(letter)


print("\n\n")
prices = {
    "banana":4,
    "apple":2,
    "orange":1.5,
    "pear":3
    }

stock = {
    "banana":6,
    "apple":0,
    "orange":32,
    "pear":15
    }

for fruit in prices:
    print(fruit)
    print("Price: %s" %prices[fruit])
    print("Stock: %s" %stock[fruit])


total=0
for key in prices:
    total=total+(prices[key]*stock[key])


print("\nTotal: %d\n" %total)

start_list=[10,50,30,20,40]
squared_list=[]
for number in start_list:
    squared_list.append(number**2)


print("Original list:")
print(start_list)
squared_list.sort()
print("Squared list:")
print(squared_list)

print("\n")
choices=['pizza','burguer','pasta','salad', 'milkshake']
print("\n")

for index, item in enumerate(choices):
    print((index+1), item)

print("\n")

list_a=[3, 9, 17, 15, 19]
list_b=[2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a,b in zip(list_a,list_b):
    if a>b:
        print(a)
    else:
        print(b)

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