def main():
    age = int(input("Input a dog's age in human years: "))
    if age < 0:
        print("Age must be positive")
        main()
    elif age <= 2:
        dog_age = age * 10.5
    else:
        dog_age = 21 + (age - 2)*4

    print("The dog age in dog years is", dog_age)
    exit()

if __name__ == '__main__':
    main()
