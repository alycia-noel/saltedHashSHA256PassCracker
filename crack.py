import itertools
import hashlib
import time 
import re

partOneAllowedChars = "abcdefghijklmnopqrstuvwxyz"
partTwoAllowedChars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
partThreeAllowedChars = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
partFourAllowedChars = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ$#%&*()"

def selectPart():
    part= input("What part would you like to test: ")
    if part == '1':
        stringType = partOneAllowedChars
    elif part == '2':
        stringType = partTwoAllowedChars
    elif part == '3':
        stringType = partThreeAllowedChars
    elif part == '4':
        stringType = partFourAllowedChars
    else:
        print("You entered an invalid part number. Try again.")
        selectPart()
    return stringType

def readFile():
    f = open("pwd.txt", "r")
    a = f.read()
    info = re.findall(r"[\w']+", a)
    user = info[0]
    salt = info[1]
    h = info[2]
    f.close()
    return(h, salt)


def tryPassword(hashp, stringTypeSet, sal):
    start = time.time()
    chars = stringTypeSet
    attempts = 0
    for i in range (1, 6):
        for letter in itertools.product(chars, repeat=i):
            attempts += 1
            letter = ''.join(letter)
            ps = (letter+sal).encode('utf-8')
            if (hashlib.sha256(ps).hexdigest()) == hashp:
                end = time.time()
                distance = end - start
                return (letter, attempts, distance)
    #print(sal)


#tries, timeAmount = tryPassword(password, stringType)
#print("Cracked the password in %s in %s tries and %s seconds!" % (password, tries, round(timeAmount, 2)))

stringType = selectPart()
hs, sa = readFile()

password, tries, timeAmount = tryPassword(hs, stringType, sa)
print("Cracked the password %s in %s tries and %s seconds!" % (password, tries, round(timeAmount, 2)))