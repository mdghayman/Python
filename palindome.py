def pal():
    word = input('\nPlease enter your word: ')

    if word == word[::-1]:
        print('Yes, your word is a palindrome.')
    else:
        print('Sorry, this word is not a palindrome.')


def main():
    print('\nStep into the the Palindome!\nEnter a word, to see whether it\'s a palindrome.')

    while True:
        pal()

        rep = input('Replay? (y/n)')

        if rep is 'y':
            True
        elif rep is 'n':
            print('Thanks for playing. Hope to see you soon.')
            return
        else:
            print('This is not a valid entry.')
            return

main()
