def main():
    starting_number = int(input("Enter an Integer: "))
    number = starting_number
    factors = []
    while number != 1:
        if (starting_number % number) == 0:
            factors.append(number)
            number -= 1
        else:
            number -=1
    factors.append(number)
    print("The factors of ", str(starting_number), "are ", str(factors))

if __name__ == '__main__':
    main()