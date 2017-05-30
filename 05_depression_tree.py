import time


def intro():
    print("Feeling down?")
    time.sleep(1)
    print("Welcome to the depression tree.")
    time.sleep(1)
    print("It's a tool to help you feel okay.")
    time.sleep(1)
    print("Answer the following 'yes' or 'no' questions.")
    time.sleep(1)
    print("The tree will tell you what to do.")
    time.sleep(1)
    sleep()


def sleep():
    time.sleep(1)
    need_sleep = input("Do you need to sleep? (y/n)")
    if need_sleep is 'y':
        print("Get some sleep.")
    elif need_sleep is 'n':
        eat()
    else:
        print("Invalid entry.")
        sleep()


def eat():
    need_eat = input("Do you need to eat? (y/n)")
    if need_eat is 'y':
        food()
    elif need_eat is 'n':
        exercise()
    else:
        print("Invalid entry.")
        eat()


def food():
    have_food = input("Do you have enough food on you? (y/n)")
    if have_food is 'y':
        print("Make something to eat, and eat it.")
    elif have_food is 'n':
        print("Buy yourself something to eat, then buy food supplies.")
    else:
        print("Invalid entry.")
        food()


def exercise():
    had_exercise = input("Have you gotten exercise today? (y/n)")
    if had_exercise is 'y':
        outside()
    elif had_exercise is 'n':
        print("Go for a run.")
    else:
        print("Invalid entry.")
        exercise()


def outside():
    been_outside = input("Have you been outside today? (y/n)")
    if been_outside is 'y':
        laugh()
    elif been_outside is 'n':
        rain()
    else:
        print("Invalid entry.")
        outside()


def laugh():
    laughed_today = input("Have you laughed today? (y/n)")
    if laughed_today is 'y':
        spoken()
    elif laughed_today is 'n':
        print("Watch an episode of a funny show.")
    else:
        print("Invalid entry.")
        laugh()


def rain():
    raining = input("Is it raining? (y/n)")
    if raining is 'y':
        print("Go to an art exhibition.")
    elif raining is 'n':
        print("Sit in a park, and read a book.")
    else:
        print("Invalid entry.")
        rain()


def spoken():
    spoken_friend = input("Have you spoken to a friend today? (y/n)")
    if spoken_friend is 'y':
        read_book()
    elif spoken_friend is 'n':
        friend()
    else:
        print("Invalid entry.")
        spoken()


def read_book():
    read_book_today = input("Have you read a book that excites you today? (y/n)")
    if read_book_today is 'y':
        print("Pack a bag, and seek adventure somewhere you've never been before.")
    elif read_book_today is 'n':
        have_book()
    else:
        print("Invalid entry.")
        read_book()


def have_book():
    have_book_today = input("Do you have a book that excites you? (y/n)")
    if have_book_today is 'y':
        print("Read your book.")
    elif have_book_today is 'n':
        print("Buy a book that excites you.")
    else:
        print("Invalid entry.")
        have_book()


def friend():
    friend_available = input("Is there a friend nearby, available for an adventure? (y/n)")
    if friend_available is 'y':
        print("Visit your friend, and plan an adventure.")
    elif friend_available is 'n':
        phone()
    else:
        print("Invalid entry.")
        friend()


def phone():
    phone_friend = input("Is there a friend available for a phone call? (y/n)")
    if phone_friend is 'y':
        print("Phone your friend, and ask how they're going.")
    elif phone_friend is 'n':
        print("Write a letter to your friend.")
    else:
        print("Invalid entry.")
        phone()

intro()
