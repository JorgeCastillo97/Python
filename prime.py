def main():
    print("MAIN FUNCTION")
    x=int(input("Type a number: "))
    print(prime(x))

def prime(x):
    if x<2:
        return False
    else:
        for aux in range(2,x-1):
            if x%aux==0:
                return False
        return True


if __name__ == '__main__':
    main()