#import math
#import numpy as np
#import os
import secrets
import string

alphanumeric = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26, 'A':27, 'B':28, 'C':29, 'D':30, 'E':31, 'F':32, 'G':33, 'H':34, 'I':35, 'J':36, 'K':37,'L':38,'M':39, 'N':40, 'O':41, 'P':42, 'Q':43, 'R':44, 'S':45, 'T':46, 'U':47, 'V':48, 'W':49, 'X':50, 'Y':51, 'Z':52, '0':53, '1':54, '2':55, '3':56, '4':57, '5':58, '6':59, '7':60, '8':61, '9':62}
inv_alphanumeric = {v-1: k for k, v in alphanumeric.items()}

def vigenere():
    pwlen = 1
    characters = []
    cipherchars = []
    alphabet = string.ascii_letters + string.digits
    keystring = ''.join(secrets.choice(alphabet) for i in range(pwlen))
    characterskey = list(keystring)
    
    for i in range(pwlen):
        n1 = characters[i]
        x1 = alphanumeric[n1]

        n2 = characterskey[i]
        x2 = alphanumeric[n2]

        ciphernum = x1 % x2
        cipherchar = inv_alphanumeric[ciphernum]
        cipherchars.append(cipherchar)
        i =+ 1

    cipher = ''.join(cipherchars)
    print(cipher)

vigenere()

def Feistel():
    global Ln, Rn
    split = []
    Ln = []
    Rn = []

    pw = str(input('password? (Alphanumeric): '))
    characters = list(pw)
    pwlen = int(len(pw))
    
    for i in range(pwlen):
        n1 = characters[i]
        x1 = alphanumeric[n1]
        split.append(x1)

    splitlen = len(split)
    midint = splitlen // 2

    left = slice(split[:midint])
    right = slice(split[midint:])
    ln.append(left)
    Rn.append(right)

    return Rn