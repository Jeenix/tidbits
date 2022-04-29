# quadratic formula
from math import sqrt
A = 1
B = 5
C = 6


def main():
    sol1 = ((B*-1) + sqrt((B ** 2) - (4 * A * C))) / (2 * A)
    sol2 = ((B*-1) - sqrt((B ** 2) - (4 * A * C))) / (2 * A)
    print("If A =", str(A), ", B = ", str(B), ", C = ", str(C), "then the solutions are ", str(sol1), "and", str(sol2))

if __name__ == '__main__':
    main()
