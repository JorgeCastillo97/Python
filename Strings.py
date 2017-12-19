meal=44.50
tax=0.0675
tip=0.15

meal+=(meal*tax)
total= meal+(meal*tip)

print("Total: $%.2f" % total)
print("Thank you for coming to \'A Rest\'!!")

restaurant_name='A REST'
first=restaurant_name[0]
second=restaurant_name[1]
third=restaurant_name[2]
fourth=restaurant_name[3]
fifth=restaurant_name[4]
sixth=restaurant_name[5]
print("\n"+first+second+third+fourth+fifth+sixth)
length=len(restaurant_name)
print("Length: "+str(length))
print("\nto lower case:"+restaurant_name.lower())
print("\nto UPPER CASE:"+restaurant_name.upper())
print("\nThe cost of the meal was:"+str(meal))
print("The tax was: %s" %str(tax))
name=input("What\'s your name: ")
print("We are pleased " \
      "for your visit dear %s"%name)

input("Press any key to continue...")