#Salted Hash sha256 password generator 
#Alycia N. Carey
#Info Sec Spring 2019 

import hashlib
import re
import random
import string


partOneAllowedChars = "^[a-z]*$"
partTwoAllowedChars = "^[a-zA-Z]*$"
partThreeAllowedChars = "^[a-zA-Z0-9]*$"
partFourAllowedChars = "^[$#%&*()a-zA-Z0-9]*$"


def getInput(allowedstring):
    user = input("Please input a username: ")
    password = input("Please input a password: ")
    if not re.match(allowedstring, password):
        print("You input an invalid character.")
        getInput(allowedstring)
    elif len(password) < 2 or len(password) > 5:
        print("You input the wrong size password. Please try again.")
        getInput(allowedstring)
    print("\nYou input:\n---------------\nusername:" + user + "\npassword:" + password)
    hash(user, password)

def selectPart():
    part= input("What part would you like to test: ")
    if part == '1':
        getInput(partOneAllowedChars)
    elif part == '2':
        getInput(partTwoAllowedChars)
    elif part == '3':
        getInput(partThreeAllowedChars)
    elif part == '4':
        getInput(partFourAllowedChars)
    else:
        print("You entered an invalid part number. Try again.")
        selectPart()

def hash(u, p):
    salt = ''.join([random.choice(string.ascii_letters + string.digits) for x in range(32)])
    ps = (p+salt).encode('utf-8')
    pwdhash = hashlib.sha256(ps).hexdigest()
    print("salt:" + salt + "\nps:" + p+salt)
    print("The generated hashed password is: [" + u + ", " + salt + ", " + pwdhash + "]")
    write(pwdhash, u, salt)

def write(ph, u, s):
    f = open("pwd.txt", "w")
    f.write("[" + u + "," + s + "," + ph + "]")
    f.close()

selectPart()

