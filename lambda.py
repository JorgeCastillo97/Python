

def main():
    """
    Lambdas (anonymous/unnamed functions) create a function to be called later
    General Form:
    lambda arg1, arg2, ..., argN : [Expression using args]
    >>lambda is an expression, not a statement
    >>lambda's body is a single expression, not a block  of statements
    """
    f = lambda x, y, z: x + y + z

    print(f(10, 20, 30))

    x = (lambda a='fee', b='fie', c='foe': a + b + c)
    print(x('Oto', 'rrino', 'laringologo.'))

    L = [lambda x: x ** 2, lambda x: x ** 3, lambda x: x ** x]

    for l in L:
        print(l(5), end=' ')

    lower = lambda i, j: i if i < j else j


if __name__ == '__main__':
    main()
