def main():
    print("Insert lengths of three sides of a triangle to confirm if it is a valid triangle.")
    a=float(input("What is value a?"))
    b=float(input("What is value b?"))
    c=float(input("What is value c?"))
    triangle = check(a,b,c)
    if triangle == 1:
        print("Yes it is a Isosceles triangle")
    elif triangle == 2:
        print("This is a scalene triangle")
    elif triangle == 3:
        print("This is a equilateral triangle")
    else:
        print("No it is not a triangle")


def check(a,b,c):
    if a == 0 or b == 0 or c == 0:
        triangle = 0
    else:
        if a + b >= c and b + c >= a and c + a >= b:
            if a == b and b == c:
                triangle = 3
            elif a == b or b == c or a == c:
                triangle = 1
            else:
                triangle = 2
        else:
            triangle = 0
    return triangle

if __name__ == '__main__':
        main()