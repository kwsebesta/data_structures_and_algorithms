import math


def karatsuba(x, y):
    """Karatsbua algorithm for multiplication"""
    if (x < 10) or (y < 10):
        return x * y

    # get minimum size
    n = min(int(math.log10(x)) + 1, int(math.log10(y)) + 1)
    n2 = n // 2

    a = int(x / 10 ** n2)
    b = int(x % 10 ** n2)
    c = int(y / 10 ** n2)
    d = int(y % 10 ** n2)

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    k = karatsuba(a + b, c + d) - ac - bd  # =ad+bc
    return (10 ** (n2 * 2)) * ac + (10 ** n2) * k + bd


def main():
    print(karatsuba(12345, 6789))


if __name__ == "__main__":
    main()
