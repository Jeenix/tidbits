from typing import List
#ceaser cypher script only works for lowercase alphabet characters

def main():
    sentence = input("What phrase would you like to encrypt?")
    num = input("What is your shift?")
    num = int(num)
    letters = []
    phrase = []
    for i, c in enumerate(sentence):
       letters.append(chr(ord(c)))
       char_num = ord(c)
       if (char_num + num) <= 122:
        phrase.append(chr(char_num + num))
       else:
        phrase.append(chr(char_num + (num-26)))
    print(letters)
    print(phrase)

if __name__ == '__main__':
    main()
