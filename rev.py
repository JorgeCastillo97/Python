def main():
    string = str(input("Enter a sentence: "))
    print("Your sentence reversed is %s" %(reverse(string)))

def reverse(word):
    l = len(word)-1
    str_reversed = ""
    while(l>=0):
        str_reversed = str_reversed + word[l]
        l-=1
    return str_reversed

if __name__ == '__main__':
    main()