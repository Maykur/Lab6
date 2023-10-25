import sys


# Partner: Adrian Nucete

def encode(password):
    encodedString = ''
    for i in password:
        encodedString += str(int(i) + 3)
    print('Your password has been encoded and stored!')
    print()
    return encodedString

def decode(password):
    decodedString = ''
    for n in password:
        decodedString += str(int(n) - 3)
    print(f"The encoded password is {password}, and the original password {decodedString}.")
    print("")

def main():
    encoded = None

    while True:
        print('Menu')
        print('-' * 13)
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        print()

        userInput = int(input('Please enter an option: '))
        if userInput == 1:
            password = input('Please enter your password to encode: ')
            encoded = encode(password)

        elif userInput == 2:
            decode(encode)


        elif userInput == 3:
            sys.exit()


if __name__ == '__main__':
    main()
