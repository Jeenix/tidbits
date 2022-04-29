def main():
    import random
    target_num, guess_num = random.randint(1, 100), 0
    while target_num != guess_num:
        guess_num = int(input('Guess a number between 1 and 100 until you get it right : '))
    print('Well guessed!')

if __name__ == '__main__':
    main()

