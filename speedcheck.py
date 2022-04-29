SPEED_LIMIT = 70

def main():
    speed = int(input("In Km/hr, What was the speed of the car?"))
    if speed > SPEED_LIMIT:
        print("Points: ", str((speed - SPEED_LIMIT)//5))
        if ((speed - SPEED_LIMIT)//5) > 12:
            print("Licence suspended")
    else:
        print("Ok")

if __name__ == '__main__':
    main()