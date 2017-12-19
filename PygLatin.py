pyg="ay"
original=input("Enter a word: ")

if len(original) > 0 and original.isalpha():
    word=original.lower()
    first=word[0]
    new=word+first+pyg
    new=new [1:len(new)]
    print(new)
else:
    print('Empty')