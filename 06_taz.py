import time


def intro():
    print("Where will we follow our travellers on this week's episode?")
    time.sleep(0.75)
    print("It's the Adventure Zone!")


def char():
    time.sleep(0.75)
    character = input("Select character:\n1. Magnus\n2. Merle\n3. Tako")
    if character == '1':
        time.sleep(0.75)
        print("Welcome, Magnus!")
        magnus()
    elif character == '2':
        time.sleep(0.75)
        print("Welcome, Merle!")
        merle()
    elif character == '3':
        time.sleep(0.75)
        print("Welcome, Tako!")
        tako()
    else:
        print('Invalid entry.')
        char()


def magnus():
    time.sleep(0.75)
    print("Time to suit up.")
    time.sleep(0.75)
    print("Suit of armour, that is.")


def merle():
    time.sleep(0.75)
    print("Get ready to heal.")
    time.sleep(0.75)
    print("Get ready to feel.")


def tako():
    time.sleep(0.75)
    print("Time to let loose.")
    time.sleep(0.75)
    print("Looks like things are about to get spicy.")

intro()

char()
