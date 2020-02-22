import random


def keyFinder():
    try:
        accountKey = input("What account are you looking for?")
        with open('allpsswrds.txt', 'r') as file:
            for line in file:
                if accountKey in line:
                    print("Here is your key for: " + accountKey)
                    print(line)
    except:
        print("An error occurred during the process, sorry please try again.")


def keyMaker():
    file = open('allpsswrds.txt', 'a')

    email = input("What email did you use?")
    uName = input("What username did you use?")
    account = input("What is this for?")

    gen_psswrd = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

    list_of_char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                    'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7',
                    '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
    ugly_pass = random.sample(list_of_char, len(gen_psswrd))

    real_pass = (''.join(ugly_pass))

    keys = "email: " + str(email) + " | uname: " + str(uName) + " | account: " + str(account) + " | password: " + str(
        real_pass)

    print("Here is the key for " + account)
    print(keys)

    file.write('\n')
    file.write(keys)
    file.close()


def customKey():
    file = open('allpsswrds.txt', 'a')

    email = input("What email did you use?")
    uName = input("What username did you use?")
    account = input("What account is this for?")
    password = input("What would you like your password to be?")

    keys = "email: " + str(email) + " | uname: " + str(uName) + " | account: " + str(account) + " | password: " + str(
        password)

    print("Here is the key for " + account)
    print(keys)

    file.write('\n')
    file.write(keys)
    file.close()


runAgain = "yes"

print("This Program is to make a key for an account, and once made can be searched upon in the file it makes. \n"
          " A key is the account that this is for,the username used, \n"
          "the password, either randomly made or custom made by you, \n"
          "and the email used for the account that you are storing. \n"
          "\n"
          "Have fun and stay safe!\n")

while runAgain == "yes" or runAgain == "y" or runAgain == "Yes" or runAgain == "Y":

    task = input("Are you finding a key or, making a key?")

    if task == "finding" or task == "Finding" or task == "f" or task == "F" or task == "find" or task == "Find":
        keyFinder()
    elif task == "making" or task == "Making" or task == "m" or task == "M" or task == "make" or task == "Make":
        typeOfKey = input("Do you want to make a random key or, make a custom key?")
        if typeOfKey == "random" or typeOfKey == "Random" or typeOfKey == "r" or typeOfKey == "R":
            keyMaker()
            print("\n")
        elif typeOfKey == "custom" or typeOfKey == "Custom" or typeOfKey == "c" or typeOfKey == "C":
            customKey()
            print("\n")
        else:
            print("That's not a valid option.")
    else:
        print("That's not a valid option.")
    runAgain = input("Do you want to run the program again?")

