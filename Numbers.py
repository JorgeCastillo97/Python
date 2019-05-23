import math, random

def main():
    # Basic Operator
    n = 123 + 456
    s = 12.365 - 9.05
    m = 1.5 * 4
    d = 45.02 / 32.07

    # 2 to the power 100
    p = 2 ** 100

    # Math functions and constants
    math.sqrt(121)
    math.pow(7, 3)
    math.factorial(10)
    math.sin(75)
    math.cos(75)
    math.tan(90)
    math.pi
    math.e
    math.tau

    # Hoy many digits in a really big number
    len(str(2 * 1000000))

    # Random numbers
    random.random()
    random.choice([n for n in range(1, 101)])


if __name__ == '__main__':
    main()
